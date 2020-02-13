
i = 0

while true
    print "Enter your number : "
    string = gets.chomp
    number = string.to_i
    toGuess = 0
    
    if string == "q" || string == "" 
        exit
    elsif number == 0 && string != "0"
        puts "Please enter integer."
    end

    if number != 0 || string == "0"
        i += 1
        if number > toGuess
            puts "Your number #{number} is too big"
        elsif number < toGuess
            puts "Your number #{number} is too small"
        else
            puts "You are find the good number"
            exit
        end
        if i >= 4
            if toGuess.even?
                puts "Your number is peer."
            else
                puts "Your number is odd."
            end
        end
    end
end



for $x in (1..number)
    number -= 1
    puts(" " * number + ("#" * $x))
end


# $i = 0
# $num = 5

# while $i < $num  do
#    puts("Inside the loop i = #$i number(s)")
#    $i +=1
# end
