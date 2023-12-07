package main.scala.day6

import scala.io.Source
import scala.math._
import scala.compiletime.ops.int

def findRange(time: Int, distance: Int): (Int, Int) = {
  val start = ((-time + sqrt(pow(time, 2)-(4*(-1)*(-distance))))/(2*(-1)))
  val end = ((-time - sqrt(pow(time, 2)-(4*(-1)*(-distance))))/(2*(-1)))
  (start.floor.toInt+1, end.ceil.toInt-1)
}

def solve : Unit = {
  val filename = "data/day6-input"
  val raceInfo = Source.fromFile(filename).getLines()
  val intRegex = """\d+""".r
  val times = intRegex.findAllMatchIn(raceInfo.next()).map(_.group(0).toInt)
  val distances = intRegex.findAllMatchIn(raceInfo.next()).map(_.group(0).toInt)

  val raceResults = (times zip distances).map((t:Int, d:Int) => findRange(t,d)).map((r) => r._2 - r._1 +1).reduce(_ * _)
  println(raceResults)

  println("__Day 6__")
}
