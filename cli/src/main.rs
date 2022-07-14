mod args;

use jenot;

use crate::args::parse_args;

fn main() {
    let args = parse_args();
    println!("{:#?}", &args);
    println!("{}", jenot::stub());
}
