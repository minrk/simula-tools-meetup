use std::collections::HashSet;
use std::fs;

fn compute_priority(item: &char) -> u32 {
    if item.is_ascii_uppercase() {
        *item as u32 - 65 + 27
    } else {
        *item as u32 - 96
    }
}

fn compute_total(rucksack: &str) -> u32 {
    let size = rucksack.len() / 2;
    let (fst, snd) = rucksack.split_at(size);
    let fst_set: HashSet<char> = fst.chars().collect();
    let snd_set: HashSet<char> = snd.chars().collect();
    let common_item = fst_set.intersection(&snd_set).into_iter().next().unwrap();
    compute_priority(common_item)
}

fn compute_total_part1(text: &str) -> u32 {
    text.trim()
        .split("\n")
        .map(|x| x.trim())
        .map(compute_total)
        .sum()
}

fn main() {
    let file_path = "input.txt";
    let contents = fs::read_to_string(file_path).expect("Should have been able to read the file");
    let total = compute_total_part1(&contents);

    println!("Part 1: {}", total);
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_compute_total_part1() {
        let example_input = "
        vJrwpWtwJgWrhcsFMMfFFhFp
        jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
        PmmdzqPrVvPwwTWBwg
        wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
        ttgJtRGJQctTZtZT
        CrZsJsPPZsGzwwsLwLmpwMDw
        ";
        assert_eq!(compute_total_part1(example_input), 157);
    }
}
