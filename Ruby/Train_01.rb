print "Enter your number : "
$number = gets.chomp

$number = $number.to_i

for $x in (1..$number)
   $number -= 1
      puts(" " * $number + ("#" * $x))
end


# $i = 0
# $num = 5

# while $i < $num  do
#    puts("Inside the loop i = #$i number(s)")
#    $i +=1
# end
