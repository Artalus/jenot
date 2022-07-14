use clap::{App, Arg, ArgMatches};

#[derive(Debug)]
pub struct Args {
    jenkins_url: String,
    user: String,
    token: String,
    notify_print: bool,
    build: String,
}

pub fn parse_args() -> Args {
    let matches = App::new("jenot-cli")
        // .version(create_version!())
        .about("CLI client for Jenot")
        .arg(
            Arg::with_name("jenkins_url")
                .short('j')
                .long("--jenkins")
                .takes_value(true)
                .help(""),
        )
        .arg(
            Arg::with_name("user")
                .short('u')
                .long("--user")
                .takes_value(true)
                .help(""),
        )
        .arg(
            Arg::with_name("token")
                .short('t')
                .long("--token")
                .takes_value(true)
                .help(""),
        )
        .arg(Arg::with_name("notify_print").long("--n-print").help(""))
        .arg(
            Arg::with_name("build")
                .required(true)
                .takes_value(true)
                .help(""),
        )
        .get_matches();
    return construct_args(&matches);
}

fn construct_args(matches: &ArgMatches) -> Args {
    let unwrap = |key: &'static str| -> String {
        let opt: Option<&String> = matches.get_one(key);
        opt.unwrap_or_else(|| panic!("missing argument: {}", key))
            .to_owned()
    };

    Args {
        jenkins_url: unwrap("jenkins_url"),
        user: unwrap("user"),
        token: unwrap("token"),
        build: unwrap("build"),
        notify_print: matches.contains_id("notify_print"),
    }
}
