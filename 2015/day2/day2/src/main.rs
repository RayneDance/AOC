use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {

    let filename = "C:/Users/jorda/Personal Projects/AOC/2015/day2/input.txt";

    let file = File::open(filename).expect("Unable to open file");
    let reader = BufReader::new(file);
    let mut paper: u32 = 0;
    let mut ribbon: u32 = 0;

    for line_result in reader.lines() {
        let line = line_result.expect("Unable to read line");
        let dims: Vec<u32> = line
            .split('x')
            .map(|dim| dim.parse::<u32>().expect("NaN"))
            .collect();

        paper = paper + calc_paper(&dims);
        ribbon = ribbon + calc_ribbon(&dims);
    }
    println!("Paper length: {}", paper);
    println!("Ribbon length: {}", ribbon)
}

fn calc_paper(dims: &Vec<u32>) -> u32{
    if let (Some(l), Some(w), Some(h)) = (dims.get(0), dims.get(1), dims.get(2)){
        let d1 = l*w;
        let d2 = w*h;
        let d3 = h*l;
        let extra = std::cmp::min(d1, std::cmp::min(d2, d3));

        2*(d1+d2+d3) + extra
    }
    else {
        panic!("Invalid dimensions: {:?}", dims);
    }
}

fn calc_ribbon(dims: &Vec<u32>) -> u32 {
    if let [l, w, h] = dims.as_slice() {
        let mut vals = [*l, *w, *h];
        vals.sort_unstable();

        let perimeter = 2 * (vals[0] + vals[1]);
        let volume = (*l) * (*w) * (*h);

        perimeter + volume
    } else {
        panic!("Invalid dimensions: {:?}", dims);
    }
}