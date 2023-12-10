package main.scala.day8

import scala.annotation.tailrec
import scala.io.Source

def mapToMap(paths: List[String]): Map[String, (String, String)] = {
    val mapRegex = """(?<location>\w{3}) = \((?<left>\w{3}), (?<right>\w{3})\)""".r
    paths.map(mapRegex.findFirstMatchIn(_)).map(
        _ match {
            case None => ("", ("", ""))
            case Some(value) => (value.group("location") -> (value.group("left"), value.group("right")))
        }
    ).toMap
}

@tailrec
def navigate(map: Map[String, (String, String)], directions: String, location: String, distance: Int): Int = {
    if(location == "ZZZ") {
        distance
    } else {
        navigate(map, directions, if(directions.charAt(distance%directions.length())=='L') {
            map.getOrElse(location, ("",""))._1
        } else {
            map.getOrElse(location, ("",""))._2
        }, distance+1)
    }
}

@tailrec
def navigateGhosts(map: Map[String, (String,String)], directions: String, location: String, distance: Int): Int = {
    val endRegex = """\w\wZ""".r
    if(endRegex.matches(location)) {
        distance
    } else {
        navigateGhosts(map, directions, if(directions.charAt(distance%directions.length())=='L') {
            map.getOrElse(location, ("",""))._1
        } else {
            map.getOrElse(location, ("",""))._2
        }, distance+1)
    }
}

@tailrec
def gcd(a: Long, b: Long) : Long ={
    if(b==0) {
        a
    } else {
        gcd(b, a % b)
    }
}

def lcm(a: Long, b: Long) : Long = {
    scala.math.abs(a*b)/gcd(a,b)
}

def solve: Unit = {
    val filename = "data/day8-input"
    val lines = Source.fromFile(filename).getLines().toList

    println("__Day 8__")
    val directions = lines.head
    val paths = lines.tail.tail
    val map = mapToMap(paths)
    println(s"Part 1: ${navigate(map, directions, "AAA", 0)}")


    val startRegex = """\w\wA""".r
    val startingPoints = map.toList.map(_._1).filter(startRegex.matches(_))
    val endLocations = startingPoints.map(navigateGhosts(map, directions, _, 0).toLong)
    println(endLocations)
    println(s"Part 2: ${endLocations.reduce(lcm(_,_))}")
}
