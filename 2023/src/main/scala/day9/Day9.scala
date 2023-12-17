package main.scala.day9

import scala.annotation.tailrec
import scala.io.Source

def nextRow(row: List[Long]): List[Long] = {
    @tailrec
    def foo(input: List[Long], output: List[Long]): List[Long] = {
        if(input.length <= 1) {
            return output
        } else {
            foo(input.tail, output.appended(input.tail.head - input.head))
        }
    }
    foo(row, List[Long]())
}


def nextValue(row: List[Long]): Long = {
    @tailrec
    def foo(row: List[Long], upperLast: Long): Long = {
        if(row.filter(_!=0).toList.length==0){
            upperLast
        } else {
            foo(nextRow(row), row.last+upperLast)
        }
    }
    foo(row, 0)
}

def previousValue(row: List[Long]): Long = {
    @tailrec
    def foo(row: List[Long], upperFirst: Long): Long = {
        if(row.filter(_!=0).toList.length==0) {
            -upperFirst
        } else {
            foo(nextRow(row), row.head-upperFirst)
        }
    }
    foo(row,0)
}


def solve: Unit = {
    val filename = "data/day9-input"
    val lines = Source.fromFile(filename).getLines().toList

    println("__Day 9__")

    val intRegex = """-?\d+""".r
    val part1Results = lines.map(intRegex.findAllMatchIn(_).map(_.group(0).toLong).toList).map(nextValue(_)).reduce(_+_)
    println(s"Part 1: ${part1Results}")
    val part2Results = lines.map(intRegex.findAllMatchIn(_).map(_.group(0).toLong).toList).map(previousValue(_)).reduce(_+_)
    println(s"Part 2: $part2Results")
}
