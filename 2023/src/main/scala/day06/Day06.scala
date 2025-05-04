package main.scala.day06

import scala.io.Source
import scala.math._
import scala.compiletime.ops.int

def findRange(time: Long, distance: Long): (Long, Long) = {
  val start = ((-time + sqrt(pow(time, 2)-(4*(-1)*(-distance))))/(2*(-1)))
  val end = ((-time - sqrt(pow(time, 2)-(4*(-1)*(-distance))))/(2*(-1)))
  (start.floor.toLong+1, end.ceil.toLong-1)
}

def solve : Unit = {
  val filename = "data/day06-input"
  val race1Info = Source.fromFile(filename).getLines()
  val intRegex = """\d+""".r
  val times = intRegex.findAllMatchIn(race1Info.next()).map(_.group(0).toLong)
  val distances = intRegex.findAllMatchIn(race1Info.next()).map(_.group(0).toLong)

  println("__Day 6__")

  val race1Results = (times zip distances).map((t:Long, d:Long) => findRange(t,d)).map((r) => r._2 - r._1 +1).reduce(_ * _)
  println(s"Part 1: $race1Results")

  val race2Info = Source.fromFile(filename).getLines()
  val time2 = intRegex.findAllMatchIn(race2Info.next()).map(_.group(0)).reduce(_+_).toLong
  val distance2 = intRegex.findAllMatchIn(race2Info.next()).map(_.group(0)).reduce(_+_).toLong

  val race2Results = findRange(time2, distance2)
  println(s"Part 2: ${race2Results._2 - race2Results._1 + 1}")
}
