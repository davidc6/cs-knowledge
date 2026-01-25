use std::{pin::Pin, task::{Context, Poll}};
use std::future::Future;

// pub enum PollOwn<T> {
//     Ready(T),
//     Pending
// }
// 
// pub trait FutureOwn {
//     type Output;
//     fn poll(self: Pin<&mut Self>, context: &mut Context) -> PollOwn<Self::Output>;
// }

struct CharCounter<F> {
    inner: F
}

impl<F> Future for CharCounter<F>
where
    F: Future<Output = String>
{
    type Output = usize;

    // Pin, a wrapper type guarantees that the value inside cannot be moved in memory.
    fn poll(mut self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output> {
        // Cannot move out of a pinned field so need to safely project 
        // the pin to inner future.
        let inner: Pin<_> = unsafe { self.as_mut().map_unchecked_mut(|s| &mut s.inner) };

        // Delegate polling to inner future
        // a. If/when the future is ready count the number of characters
        // b. Else pending
        let p = match inner.poll(cx) {
            Poll::Ready(s) => Poll::Ready(s.chars().count()),
            Poll::Pending => Poll::Pending
        };
        p
    }
}

// Future Combinators.
// These allow to chain futures together.
// Methods like map() make it possible.
fn count_chars(value: impl Future<Output = String>) -> impl Future<Output = usize> {
    CharCounter {
        inner: value
    }
}

async fn some_s() -> String {
    "aha".to_string()
}

fn main() {
    let _a = count_chars(some_s());
}

