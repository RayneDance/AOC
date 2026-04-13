use std::fs;

fn get_input() -> String {
    fs::read_to_string("input.txt")
        .expect("Failed to read input.txt")
        .trim()
        .to_string()
}

fn part1(data: &str) -> impl std::fmt::Display {
    let _ = data;
    "todo"
}

fn part2(data: &str) -> impl std::fmt::Display {
    let _ = data;
    "todo"
}

fn main() {
    let data = get_input();
    println!("Part 1: {}", part1(&data));
    println!("Part 2: {}", part2(&data));
}
