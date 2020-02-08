
bl_info = {
    "name": "POLYSWEEPER",
    "author": "Andrea Rastelli",
    "version": (0, 0, 5),
    "blender": (2, 80, 0),
    "location": "3D Viewport > Sidebar > RASTART",
    "description": "Polygon sweeper",
    "warning": "working in progress",
    "wiki_url": "",
    "category": "Mesh",
}

import bpy
import bmesh
from mathutils import Vector
from bpy.types import (
                        PropertyGroup,
                        Panel
                        )

from bpy.props import (
                        BoolProperty,
                        EnumProperty,
                        FloatProperty,
                        StringProperty,
                        IntProperty,
                        PointerProperty
                        )


class MESH_OT_polysweeper(bpy.types.Operator): #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    bl_idname = "mesh.polysweeper"
    bl_label = "polysweeper"
    bl_options = {'REGISTER', 'UNDO'}

    UserValue : FloatProperty(name="Normal Scale", default=1.0)
    sweep : BoolProperty(name="Sweep Faces", default=True)
    FaceNormal : BoolProperty(name="Use Face Normals", default=False)
    closed : BoolProperty(name="closed", default=False)
    fused : BoolProperty(name="join", default=False)    

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return (obj and obj.type == 'MESH' and context.mode == 'EDIT_MESH')

    def draw(self, context):
        layout = self.layout
        box = layout.box()

        box.prop(self, "UserValue")

        box.prop(self, "sweep")
        
        box.prop(self, "FaceNormal")

        box.prop(self, "closed")
        
        box.prop(self, "fused")
        
    def invoke(self, context, event):
        self.action(context)
        return {'FINISHED'}

    def execute(self, context):
        self.action(context)
        return {'FINISHED'}

    def action(self, context):
       
        PS(self.UserValue,self.sweep,self.FaceNormal,self.closed,self.fused)
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()
        
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
class GLOBAL_UL_polysweeper_props(PropertyGroup):
    local_profile = BoolProperty(name="local_profile", default= False,options = {'HIDDEN'})
    profile_OBJ = PointerProperty(name="prof_OBJ", type=bpy.types.Object)
    
class VIEW3D_PT_polysweeper_tool(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Rastart"
    bl_label = "POLYSWEEPER"

    @classmethod
    def poll(cls, context):
        return (
            context.active_object is not None
            and
            context.object.type == 'MESH'
        )

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.prop(context.scene.polysweeper, "local_profile")
        layout.prop(context.scene.polysweeper, "profile_OBJ")
        layout.operator("polysweeper.set_profile_obj", text="set profile")
        layout.operator("mesh.polysweeper", text="polysweep!")

class PS_set_profile_obj(bpy.types.Operator):
    bl_idname = "polysweeper.set_profile_obj"
    bl_label = ""
    bl_description = ''
    bl_context = 'mesh'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        get_profile()
        return {'FINISHED'}



classes = (
    MESH_OT_polysweeper,
    GLOBAL_UL_polysweeper_props,
    VIEW3D_PT_polysweeper_tool,
    PS_set_profile_obj
)



def register():

    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    bpy.types.Scene.polysweeper = PointerProperty(
        type = GLOBAL_UL_polysweeper_props
    )
   

def unregister():

    del(bpy.types.Scene.polysweeper)
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

if __name__ == "__main__":
    register()
    
    
#@@@@@@@@@@@@@@@@@@@@@@@@@

def PS(normal,sweep,faceNormal,closed,fused):
    U_normal= normal #normal multiplier
    obj = bpy.context.object
    me = obj.data
    
    CURSOR = bpy.context.scene.cursor.location # cursor location to orient edge loop
    bm = bmesh.from_edit_mesh(me)
    S = bmesh.from_edit_mesh(me).select_history
    
    PROFILE=[]

    BASE_PATH = set(S)#.remove(PROFILE) # PATH FACE LOOP

    if not bpy.context.scene.polysweeper.local_profile:
        
        prof_data = bpy.context.scene.polysweeper.profile_OBJ.data
        for f in prof_data.polygons:
            if f.select: S = f
        verts=[v for v in S.vertices]
        for v in verts:
            vert=prof_data.vertices[v].co
            PROFILE.append( (vert.x,vert.y,vert.z) )
        
        for f in bm.faces:
            if f.select: BASE_PATH.add(f)
    
    else:
        ACTIVE = S.active # PROFILE FACE
        ACTIVE.select = False       
        for f in bm.faces:
            if f.select: BASE_PATH.add(f)
        BASE_PATH.remove(ACTIVE)
        
        for v in ACTIVE.verts:
            PROFILE.append( (v.co.x,v.co.y,v.co.z) )
    
    PATH=set() #duplicate path loop to get better vertex normal
    for f in BASE_PATH:
        nu_f = f.copy()
        PATH.add(nu_f)
           
    for f in BASE_PATH:
        f.select=False   
    
    for f in PATH: 
        f.select=True 
    bpy.ops.mesh.remove_doubles(use_unselected=False) 


    # DEFINE PROFILE FACE ON XZ PLANE
    PxMAX=[]; PzMAX=[];
    
    for v in PROFILE:
        PxMAX.append(v[0])
         
    PxMIN=min(PxMAX); PxMAX=max(PxMAX)   # MIN MAX X 
    
    for v in PROFILE:
        if (v[0]==PxMIN):
            PzMAX.append(v[2]) 
                      
    PzMIN=min(PzMAX); PzMAX=max(PzMAX)   # MIN MAX Z     
    Zlen=PzMAX-PzMIN  # Z lenght 
     
    # PATH EDGE LOOP SET

    ET=set()

    for e in bm.edges:
        if e.select: ET.add(e) #TOTAL EDGES

    EB = set() #BORDER EDGES
    ER = set() #EDGE RING

    bpy.ops.mesh.region_to_loop()
    for e in bm.edges:
        if e.select: EB.add(e)

    def Start_edge(border_edge): #return edge under cursor

            dist=set()
            for e in border_edge:
                mx=(e.verts[0].co.x + e.verts[1].co.x)/2
                my=(e.verts[0].co.y + e.verts[1].co.y)/2
                mz=(e.verts[0].co.z + e.verts[1].co.z)/2
                median= Vector((mx,my,mz))
                dist.add((CURSOR - median).length)

            dist=min(dist) 
            start_edge=None
            for e in border_edge:
                mx=(e.verts[0].co.x + e.verts[1].co.x)/2
                my=(e.verts[0].co.y + e.verts[1].co.y)/2
                mz=(e.verts[0].co.z + e.verts[1].co.z)/2
                median= Vector((mx,my,mz))
                if ((CURSOR - median).length != dist):
                    e.select=False
                else:
                    start_edge=e #A_LOOP START

            return start_edge
        
    OPP_F=[] #opposite face in the loop

    for f in PATH: #FIND FIRST AND LAST FACES IN THE LOOP
        count=0
        for e in f.edges:
            if (e in EB): count+=1
        if (count>2): OPP_F.append(f)
      
    if (len(OPP_F)==2): #LOOP FACE CASE
        for f in OPP_F:
            opp_e = set(f.edges)&EB
            alt_v = list(set(f.edges)-opp_e)
            alt_v = alt_v[0].verts
            for e in opp_e:
                if not (e.verts[0] in alt_v or e.verts[1] in alt_v):
                    ER.add(e)

    elif (len(OPP_F)==1): #SINGLE FACE CASE
        start_edge=Start_edge(EB)
        opp_v=start_edge.verts
        for e in OPP_F[0].edges:
            if ((e.verts[0] in opp_v) ^ (e.verts[1] in opp_v)):
                ER.add(e)
                     
    EL = EB-ER  # LOOP EDGE A+B
    ER = ET-EL | ER # EDGE RING
    V_OPP= set()
    for e in (EB&ER):
        for v in e.verts: V_OPP.add((v.co.x,v.co.y,v.co.z))
    edge_A=Start_edge(EL) #A_LOOP START

    A_LOOP=set()
    A_VERTS=set()
    
    SORTED_LOOP=[]#test

    def grow_loop(edge):
        A_LOOP.add(edge)
        if not edge in SORTED_LOOP: SORTED_LOOP.append(edge)#test
        for v in edge.verts:
            links=v.link_edges
            for link in links:
                if (link in EL and link not in A_LOOP):
                    A_LOOP.add(link)
                    SORTED_LOOP.append(link)#test
                    grow_loop(link)
                              
    grow_loop(edge_A)  
    B_LOOP=EL-A_LOOP   

    for e in A_LOOP:
        for v in e.verts: A_VERTS.add(v)  

    for e in ET:
        e.select=False
        
    SWEEP=set()#sweeped geometry
    
    for e in ER:
      
        for v in e.verts: 
            if v in A_VERTS: V0=v
            else: V1 = v
        
        PROJ = V1.co-V0.co
        L = PROJ.length
        L= L/Zlen # L:x=Zlen:1
        NU_VERTS=[]
        NU_FACES=[]
        PROJ.normalize()
        S=V0.calc_shell_factor() # SCALE FACTOR ANGLE BASED
        
        if (faceNormal): # USE FACE NORMAL CASE
            normal=[]
            for face in e.link_faces:
                #if face in PATH:
                normal.append(face.normal)
            if len(normal)==1:
                normal=normal[0]
            else:
                normal=[(normal[0][0]+normal[1][0])/2,(normal[0][1]+normal[1][1])/2,(normal[0][2]+normal[1][2])/2]   

        else: # USE VERTEX NORMAL CASE
            normal=[V0.normal[0],V0.normal[1],V0.normal[2]]
                
        for v in PROFILE: # PROJECT PROFILE POINT ALONG NORMAL 
            
            z0=v[2]-PzMAX 
            x0=v[0]-PxMIN
            X=V0.co.x - ( PROJ[0]*z0*L) + ( normal[0]*x0*L*S*U_normal)
            Y=V0.co.y - ( PROJ[1]*z0*L) + ( normal[1]*x0*L*S*U_normal)
            Z=V0.co.z - ( PROJ[2]*z0*L) + ( normal[2]*x0*L*S*U_normal)

            v = bm.verts.new( (X,Y,Z) ) 
            NU_VERTS.append(v)
            SWEEP.add(v)
            
        f=bm.faces.new(NU_VERTS)
        f.select=True 

#___________________ PROFILE FACE GENERATED AND SELECTED --> SWEEP CODE ---> 
    PROFILE_FACES = set()
    
    for f in bm.faces:
        if f.select==True: PROFILE_FACES.add(f) 
              
    if (sweep==True and (len(OPP_F)==2 or len(PATH)>2) ): # ORDERED FACE SWEEP
        bpy.ops.mesh.select_all(action='DESELECT')
        
        SWEEP_FACES=set()
        last_edge=len(SORTED_LOOP)-1
        for i,e in enumerate(SORTED_LOOP):
                   
            v1=e.verts[0].co
            v2=e.verts[1].co
            
            for f in PROFILE_FACES:
                for v in f.verts:
                    if v.co == v1: 
                        f1=f.copy()
                        if closed and (v.co.x,v.co.y,v.co.z) in V_OPP: #check first edge A loop and bo
                            first_face=f.copy()
                            SWEEP_FACES.add(first_face)
                    elif v.co == v2: 
                        f2=f.copy()
                        if closed and (v.co.x,v.co.y,v.co.z) in V_OPP: #check first edge B loop
                            first_face=f.copy() 
                            SWEEP_FACES.add(first_face)
                    
            f1.select=True; f2.select=True     
            bpy.ops.mesh.bridge_edge_loops(type='SINGLE')
            for f in bm.faces:
                if f.select: SWEEP_FACES.add(f)

            bpy.ops.mesh.select_all(action='DESELECT')
            f1.select=True; f2.select=True 
            bpy.ops.mesh.delete(type='FACE')
        if len(OPP_F)==0:
            for f in PROFILE_FACES: f.select=True 
            bpy.ops.mesh.delete(type='FACE')
        for f in SWEEP_FACES:
            f.select=True       

    elif (sweep==True and len(OPP_F)==1): # SINGLE FACE SWEEP
        for f in PATH: f.select = False
        bpy.ops.mesh.bridge_edge_loops(type='SINGLE')
   
    bpy.ops.mesh.remove_doubles(use_unselected=False)
    bpy.ops.mesh.normals_make_consistent()
        
    
    bpy.ops.mesh.select_all(action='DESELECT')
    
    if fused:
        
        TWIN_FACES=set()
        FUSE_FACES=set()
        MEDIAN_VALUES = set()
     
        for f in PATH: 
            MEDIAN_VALUES.add(f.calc_center_bounds().freeze())
          
        for f in bm.faces:
            if f.calc_center_bounds().freeze() in MEDIAN_VALUES: 
                TWIN_FACES.add(f)
                f.select=True
        bpy.ops.mesh.select_linked(delimit={'SEAM'})
        
        for f in bm.faces:
             if f.select and not f in TWIN_FACES:
                 FUSE_FACES.add(f)
                   
        bpy.ops.mesh.select_all(action='DESELECT')
        for f in TWIN_FACES:f.select=True

    else:
        
        for f in PATH:f.select=True
              
    if (sweep and len(OPP_F)==2):
        for f in PROFILE_FACES:
            f.select=True
      
    bpy.ops.mesh.delete(type='FACE')
    
    if fused:
        for f in FUSE_FACES:f.select=True
        bpy.ops.mesh.remove_doubles(use_unselected=False)

        bpy.ops.mesh.select_all(action='DESELECT')
        
    bpy.ops.mesh.select_mode(type="FACE")
    bmesh.update_edit_mesh(me, True) 

active_polysweeper_mesh = None

def get_profile():
    '''
    PROF_OBJ= bpy.context.scene.polysweeper.profile_OBJ
    
    if PROF_OBJ and bpy.context.object!= PROF_OBJ:
        
        active_polysweeper_mesh =  bpy.context.object
        bpy.ops.object.editmode_toggle()
        PROF_OBJ.select_set(True)
        bpy.ops.object.editmode_toggle()
    
    elif bpy.context.object == PROF_OBJ:
        active_polysweeper_mesh.select_set(True)
       
    '''
    global active_polysweeper_mesh
    PROF_OBJ= bpy.context.scene.polysweeper.profile_OBJ
    
    if PROF_OBJ and PROF_OBJ.select_get():
        
        bpy.ops.object.mode_set(mode='OBJECT')
        PROF_OBJ.select_set(False)
        active_polysweeper_mesh.select_set(True)
        bpy.context.view_layer.objects.active=active_polysweeper_mesh
        bpy.ops.object.mode_set(mode='EDIT')
        
    
    else:
        active_polysweeper_mesh =  bpy.context.object
        
        bpy.ops.object.mode_set(mode='OBJECT')
        PROF_OBJ.select_set(True)
        active_polysweeper_mesh.select_set(False) 
        bpy.context.view_layer.objects.active=PROF_OBJ
        
        bpy.ops.object.mode_set(mode='EDIT')
        
