use std::{pin::Pin, task::{Context}};

pub enum Poll<T> {
    Ready(T),
    Pending
}

pub trait Future {
type Output;
    fn poll(self: Pin<&mut Self>, context: &mut Context) -> Poll<Self::Output>;
}

// Future Combinators - TODO

fn main() {
    println!("Hello, world!");
}
