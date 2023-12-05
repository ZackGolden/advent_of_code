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

def solve : Unit = {

    val filename = "data/day3-input"
    val lines = Source.fromFile(filename).getLines().toList
    println("__Day 3__")
    println("Part 1: " + findAdjacentComponents(lines))

}