use std::fs;

fn main() {
    let start_time = std::time::Instant::now();
    let mut sum = 0;
    for line in read_file_as_list_of_strings("files/1") {
        sum += find_first_digit(&line) * 10 + find_last_digit(&line)
    }
    println!("Sum 1: {}", sum);
    sum = 0;
    for line in read_file_as_list_of_strings("files/1") {
        let replaced_line = replace_string_to_int(&line);
        sum += find_first_digit(&replaced_line) * 10 + find_last_digit(&replaced_line)
    }
    println!("Sum 2: {}", sum);
    println!("Time: {}ms", start_time.elapsed().as_millis());
}

fn read_file_as_list_of_strings(filename: &str) -> Vec<String> {
    let contents = fs::read_to_string(filename).expect("Something went wrong reading the file");
    let lines: Vec<String> = contents.lines().map(String::from).collect();
    lines
}

fn replace_string_to_int(line: &str) -> String {
    let replaced = line
        .replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine");
    replaced
}

fn find_first_digit(line: &str) -> i32 {
    let mut first_digit = String::new();
    for c in line.chars() {
        if c.is_digit(10) {
            first_digit.push(c);
            break;
        }
    }
    first_digit.parse::<i32>().unwrap()
}

fn find_last_digit(line: &str) -> i32 {
    let mut last_digit = String::new();
    for c in line.chars().rev() {
        if c.is_digit(10) {
            last_digit.push(c);
            break;
        }
    }
    last_digit
        .chars()
        .rev()
        .collect::<String>()
        .parse::<i32>()
        .unwrap()
}
