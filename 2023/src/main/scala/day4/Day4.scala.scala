package main.scala.day4

import scala.io.Source

def score(card: String): Int = {
    val scoreRegex = """\d+""".r
    val results = card.splitAt(card.indexOf(":"))._2
    val myNumbers = scoreRegex.findAllMatchIn(results.splitAt(results.indexOf("|"))._1).map(_.group(0).toInt)
    val winningNumbers = scoreRegex.findAllMatchIn(results.splitAt(results.indexOf("|"))._2).map(_.group(0).toInt).toSet

    var score = 0
    for 
        number <- myNumbers
    do
        if(winningNumbers.contains(number)) {
            score = score + 1
        }

    if (score != 0) scala.math.pow(2,score-1).toInt else 0 
}

def solve : Unit = {
val filename = "data/day4-input"
    val scratchCards = Source.fromFile(filename).getLines().toList
    println("__Day 4__")
    println("Part 1: " + scratchCards.map(score(_)).reduce(_+_))
    println("Part 2: " )

}
