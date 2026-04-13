use std::fs;

fn main() {
    let contents = fs::read_to_string("C:/Users/jorda/Personal Projects/AOC/2015/day1/input.txt")
        .expect("Something went wrong reading the file");

    let mut count = 0;
    let mut basement_reached = false;

    for (index, character) in contents.chars().enumerate() {
        match character {
            '(' => count += 1,
            ')' => count -= 1,
            _   => println!("Unrecognized char")
        }
        if !basement_reached && count < 0 {
            basement_reached = true;
            println!("First basement: {}", index + 1);
        }
    }
    println!("{}", count)
}