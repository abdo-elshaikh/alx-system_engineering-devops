#!/usr/bin/env ruby
# script should output: [SENDER],[RECEIVER],[FLAGS]
SENDER = ARGV[0].scan(/\[from:(.*?)\]/).join
RECEIVER = ARGV[0].scan(/\[to:(.*?)\]/).join
FLAGS = ARGV[0].scan(/\[flags:(.*?)\]/).join
puts "#{SENDER},#{RECEIVER},#{FLAGS}"