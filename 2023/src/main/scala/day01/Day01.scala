package main.scala.day01

import scala.io.Source

def generateCalibrationValue(calibrationValues: List[String]) : Int = {
  calibrationValues.map(_.filter(_.isDigit)).map(_.toString()).toList.map(i => (i.head.toString() + i.last.toString()).toInt).reduce(_+_)
}

def wordToNumber(s: String) : String = {
  val numberRegex = "(?=([0-9]|one|two|three|four|five|six|seven|eight|nine|zero))".r
  var result = ""
  for patternMatch <- numberRegex.findAllMatchIn(s).map(_.group(1)) do
    val number = patternMatch match {
      case "one" | "1" => "1"
      case "two" | "2" => "2"
      case "three" | "3" => "3"
      case "four" | "4" => "4"
      case "five" | "5" => "5"
      case "six" | "6" => "6"
      case "seven"  | "7" => "7"
      case "eight" | "8" => "8"
      case "nine"  | "9" => "9"
      case "zero" | "0"=> "0"
    }
    result = result + number
  result
}

def solve: Unit =
  val filename = "data/day01-input"
  println("__Day 1__")
  println("Part 1: " + generateCalibrationValue(Source.fromFile(filename).getLines.toList))
  println("Part 2: " + generateCalibrationValue(Source.fromFile(filename).getLines.toList.map(wordToNumber(_))))

