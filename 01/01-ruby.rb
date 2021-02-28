#!/opt/ruby3.0/bin/ruby

numbers = File.open("01-input.txt").readlines.map(&:to_i)
part1 = numbers.combination(2).to_a.select {|x| 2020 == x.sum}[0].inject(:*)
part2 = numbers.combination(3).to_a.select {|x| 2020 == x.sum}[0].inject(:*)
puts part1, part2
