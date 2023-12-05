package main.scala.day3

import scala.io.Source
import scala.util.matching.Regex.Match

def findSymbols(schematics: List[String]) : List[String] = {
    var y = 0
    val symbolRegex = """[^0-9\.\n]""".r
    var results = List[String]()
    for 
        schematic <- schematics
    do
        for 
            symbol <- symbolRegex.findAllMatchIn(schematic)
        do
            results :::= List(s"${symbol.start},$y")
        y = y+1
    results
}

def sweep(partMatch: Match, line: Int, symbols: Set[String]) : Boolean = {
    var symbolInSweep = false
    for
        xSearch <- Range.inclusive(partMatch.start-1,partMatch.end)
    do
        for 
            ySearch <- Range.inclusive(line-1,line+1)
        do
            if(symbols.contains(s"$xSearch,$ySearch")) {
                symbolInSweep = true
            }
    symbolInSweep
}

def findAdjacentComponents(schematics: List[String]) : Int = {
    val symbols = findSymbols(schematics).toSet
    var y = 0
    var allParts = 0
    var unconnectedParts = 0
    val numberRegex = """[\d]+""".r
    for
        schematic <- schematics
    do
        for
            part <- numberRegex.findAllMatchIn(schematic)
        do
            if(!sweep(part, y, symbols)) {
                unconnectedParts = unconnectedParts + part.group(0).toInt
            }
            allParts = allParts + part.group(0).toInt
        y=y+1

    allParts - unconnectedParts
} 


def findGears(schematics: List[String]): List[String] = {
    var y = 0
    val symbolRegex = """[*]""".r
    var results = List[String]()
    for 
        schematic <- schematics
    do
        for 
            symbol <- symbolRegex.findAllMatchIn(schematic)
        do
            results :::= List(s"${symbol.start},$y")
        y = y+1
    results
}

def sweepAndReturnParts(partMatch: Match, line: Int, symbols: Set[String]) : List[String] = {
    var symbolsInSweep = List[String]()
    for
        xSearch <- Range.inclusive(partMatch.start-1,partMatch.end)
    do
        for 
            ySearch <- Range.inclusive(line-1,line+1)
        do
            if(symbols.contains(s"$xSearch,$ySearch")) {
                symbolsInSweep :::= List(s"$xSearch,$ySearch")
            }
    symbolsInSweep
}

def createListOfAdjacentComponents(schematics: List[String]) : Map[String, List[Int]] = {
    val symbols = findGears(schematics).toSet
    var y = 0
    val numberRegex = """[\d]+""".r
    var componentMap = Map[String, List[Int]]()
    for
        schematic <- schematics
    do
        for
            part <- numberRegex.findAllMatchIn(schematic)
        do
            for
                gear <- sweepAndReturnParts(part, y, symbols)
            do
                componentMap.get(gear) match {
                    case None => componentMap = componentMap.updated(gear, List(part.group(0).toInt))
                    case Some(value) => componentMap = componentMap.updated(gear, value :+ part.group(0).toInt)
                }
                
        y=y+1

    componentMap
} 

def solve : Unit = {

    val filename = "data/day3-input"
    val lines = Source.fromFile(filename).getLines().toList
    println("__Day 3__")
    println("Part 1: " + findAdjacentComponents(lines))
    println("Part 2: " + createListOfAdjacentComponents(lines).filter(_._2.size==2).map(_._2.reduce(_*_)).reduce(_+_))

}