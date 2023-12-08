package main.scala.day7

import scala.annotation.tailrec
import scala.io.Source

enum handTypes :
    case highCard, onePair, twoPair, threeOfaKind, fullHouse, fourOfaKind, fiveOfaKind

enum cardTypes :
    case C2, C3, C4, C5, C6, C7, C8, C9, T, J, Q, K, A

enum cardTypesJ :
    case J, C2, C3, C4, C5, C6, C7, C8, C9, T, Q, K, A

def findHandType(hand: String): handTypes = {
    val handMap = hand.groupBy(_.toChar).mapValues(_.size).toList

    handMap.size match {
        case 1 => handTypes.fiveOfaKind
        case 2 => {
            if (handMap.filter(_._2==4).size==1) {
                handTypes.fourOfaKind
            } else {
                handTypes.fullHouse
            }
        }
        case 3 => {
            if (handMap.filter(_._2==3).size==1) {
                handTypes.threeOfaKind
            } else {
                handTypes.twoPair
            }
        } 
        case 4 => {
            handTypes.onePair
        }
        case 5 => {
            handTypes.highCard
        }
    }
}

def findHandTypeWithJoker(hand: String): handTypes = {
    val handMap = hand.groupBy(_.toChar).mapValues(_.size).toMap[Char, Int]

    val jokers = handMap.getOrElse('J', 0)
    
    val handmapWJokers = if(jokers==5) {
        handMap
    } else {
        val largestSuit = handMap.removed('J').maxBy(_._2)._1
        val largestSuitSize = handMap.getOrElse(largestSuit, 0)
        handMap.removed('J').updated(largestSuit, jokers+largestSuitSize)
    }
    handmapWJokers.size match {
        case 1 => handTypes.fiveOfaKind
        case 2 => {
            if (handmapWJokers.filter(_._2==4).size==1) {
                handTypes.fourOfaKind
            } else {
                handTypes.fullHouse
            }
        }
        case 3 => {
            if (handmapWJokers.filter(_._2==3).size==1) {
                handTypes.threeOfaKind
            } else {
                handTypes.twoPair
            }
        } 
        case 4 => {
            handTypes.onePair
        }
        case 5 => {
            handTypes.highCard
        }
    }
}

def findCardType(card: Char): cardTypes = {
    card match {
        case '2' => cardTypes.C2
        case '3' => cardTypes.C3
        case '4' => cardTypes.C4
        case '5' => cardTypes.C5
        case '6' => cardTypes.C6
        case '7' => cardTypes.C7
        case '8' => cardTypes.C8
        case '9' => cardTypes.C9
        case 'T' => cardTypes.T
        case 'J' => cardTypes.J
        case 'Q' => cardTypes.Q
        case 'K' => cardTypes.K
        case 'A' => cardTypes.A
    }
}

def findCardTypeWithJoker(card: Char): cardTypesJ = {
    card match {
        case 'J' => cardTypesJ.J
        case '2' => cardTypesJ.C2
        case '3' => cardTypesJ.C3
        case '4' => cardTypesJ.C4
        case '5' => cardTypesJ.C5
        case '6' => cardTypesJ.C6
        case '7' => cardTypesJ.C7
        case '8' => cardTypesJ.C8
        case '9' => cardTypesJ.C9
        case 'T' => cardTypesJ.T
        case 'Q' => cardTypesJ.Q
        case 'K' => cardTypesJ.K
        case 'A' => cardTypesJ.A
    }
}

@tailrec
def compareValues(f: String, s: String): Boolean = {
    if(f.length()==0) {
        true
    } else if (findCardType(f.head).ordinal < findCardType(s.head).ordinal) {
        true
    } else if (findCardType(f.head).ordinal > findCardType(s.head).ordinal) {
        false
    } else {
        compareValues(f.tail, s.tail)
    }
}

@tailrec
def compareValuesWithJoker(f: String, s: String): Boolean = {
    if(f.length()==0) {
        true
    } else if (findCardTypeWithJoker(f.head).ordinal < findCardTypeWithJoker(s.head).ordinal) {
        true
    } else if (findCardTypeWithJoker(f.head).ordinal > findCardTypeWithJoker(s.head).ordinal) {
        false
    } else {
        compareValuesWithJoker(f.tail, s.tail)
    }
}

def compareHands(first: String, second: String): Boolean = {
    if(findHandType(first).ordinal < findHandType(second).ordinal) {
        true
    } else if (findHandType(first) == findHandType(second)) {
        compareValues(first, second)
    } else {
        false
    }
}

def compareHandsWithJoker(first: String, second: String): Boolean = {
    if(findHandTypeWithJoker(first).ordinal < findHandTypeWithJoker(second).ordinal) {
        true
    } else if (findHandTypeWithJoker(first) == findHandTypeWithJoker(second)) {
        compareValuesWithJoker(first, second)
    } else {
        false
    }
}

def solve: Unit = {
    val filename = "data/day7-input"
    val lines = Source.fromFile(filename).getLines().toList
    println("__Day 7__")
    val handRegex = """(?<cards>\w+) (?<bid>\d+)""".r
    val part1Result = lines.map(handRegex.findFirstMatchIn(_))
        .map(_ match {
            case None => ("", 0)
            case Some(value) => (value.group("cards"), value.group("bid").toInt)
        })
        .sortWith(lt=(A,B) => compareHands(A._1, B._1))
        .zipWithIndex
        .map(a => (a._2+1)*a._1._2)
        .reduce(_ + _)

    println(s"Part 1: $part1Result")
    val part2Result = lines.map(handRegex.findFirstMatchIn(_))
        .map(_ match {
            case None => ("", 0)
            case Some(value) => (value.group("cards"), value.group("bid").toInt)
        })
        .sortWith(lt=(A,B) => compareHandsWithJoker(A._1, B._1))
        .zipWithIndex
        .map(a => (a._2+1)*a._1._2)
        .reduce(_ + _)
    println(s"Part 2: $part2Result")
}