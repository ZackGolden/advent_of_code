package main.scala.day02

import scala.util.matching.Regex.Match
import scala.io.Source

def maxCubesFromGame(game: String) : Map[String, Int] = {
    val gameRegex = """Game (?<number>\d+):(?<rounds>.+)""".r
    val gameInfo = gameRegex.findFirstMatchIn(game)
    val gameNumber = gameInfo match {
            case None => 0
            case Some(i) => i.group("number").toInt
    }
    var results = Map[String, Int](("Game", gameNumber))

    val cubeRegex = """(?<number>\d+) (?<color>\w+)""".r
    val rounds = gameInfo match {
        case None => Iterator[Match]()
        case Some(i) => cubeRegex.findAllMatchIn(i.group("rounds"))
    }
    for color <- rounds do
        results.get(color.group("color")) match {
            case None => results = results.updated(color.group("color"), color.group("number").toInt)
            case Some(i) => results = results.updated(color.group("color"), if (i > color.group("number").toInt) i else color.group("number").toInt ) 
        }
    
    results
}

def isGamePossible(gameResults: Map[String, Int], actualCubes: Map[String, Int]): Boolean = {
    var testResult = true
    
    for result <- gameResults.toSet.iterator do
        if (result._1 != "Game") {
            actualCubes.get(result._1) match {
                case None => testResult = false
                case Some(i) => if (i<result._2) {testResult = false} 
            }
        }
        

    testResult
}

def cubePower(maxCubesFromGame: Map[String,Int]): Int = {
    maxCubesFromGame.filter(_._1 != "Game").map(_._2).reduce(_ * _)
}

def solve : Unit = {

    val filename = "data/day02-input"
    val lines = Source.fromFile(filename).getLines().toList
    val actualCubes = Map[String, Int](
        ("red", 12),
        ("green", 13),
        ("blue", 14)
    )
    println("__Day 2__")
    println("Part 1: " + lines.map(maxCubesFromGame(_)).filter(isGamePossible(_, actualCubes)).map(_.getOrElse("Game", 0)).reduce(_+_))
    println("Part 2: " + lines.map(maxCubesFromGame(_)).map(cubePower(_)).reduce(_+_))
}
