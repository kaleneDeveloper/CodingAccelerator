print "Enter your number : "
$number = gets.chomp.to_i

for $x in (1..$number)
   $number -= 1
      puts(" " * $number + ("#" * $x))
end


