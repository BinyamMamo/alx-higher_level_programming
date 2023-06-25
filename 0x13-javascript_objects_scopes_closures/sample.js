#!/usr/bin/node
console.log("hello");

function fun() {
  static num = 0;
  fun.num += 1;
  console.log(num);
}

fun();
