package main.scala.day05

import scala.io.Source

class Almanac(val seeds: List[Long], 
              val seedsToSoil: List[List[Long]], 
              val soilToFertilizer: List[List[Long]],
              val fertilizerToWater: List[List[Long]],
              val waterToLight: List[List[Long]],
              val lightToTemperature: List[List[Long]],
              val temperatureToHumidity: List[List[Long]],
              val humidityToLocation: List[List[Long]])

def parseAlmanac(lines: List[String]): Almanac = {
  val mapRegex = """(\d+) (\d+) (\d+)""".r
  val i = lines.iterator
  val seeds = i.next().split(" ").drop(1).map(_.toLong).toList
  i.next()
  i.next()
  val seedsToSoil = i.takeWhile(mapRegex.matches(_)).toList.map(_.split(" ")).map(m => List(m.apply(0).toLong, m.apply(1).toLong, m.apply(2).toLong))
  i.next()
  val soilToFertilizer = i.takeWhile(mapRegex.matches(_)).toList.map(_.split(" ")).map(m => List(m.apply(0).toLong, m.apply(1).toLong, m.apply(2).toLong))
  i.next()
  val fertilizerToWater = i.takeWhile(mapRegex.matches(_)).toList.map(_.split(" ")).map(m => List(m.apply(0).toLong, m.apply(1).toLong, m.apply(2).toLong)) 
  i.next()
  val waterToLight = i.takeWhile(mapRegex.matches(_)).toList.map(_.split(" ")).map(m => List(m.apply(0).toLong, m.apply(1).toLong, m.apply(2).toLong))
  i.next()
  val lightToTemperature = i.takeWhile(mapRegex.matches(_)).toList.map(_.split(" ")).map(m => List(m.apply(0).toLong, m.apply(1).toLong, m.apply(2).toLong))
  i.next()
  val temperatureToHumidity = i.takeWhile(mapRegex.matches(_)).toList.map(_.split(" ")).map(m => List(m.apply(0).toLong, m.apply(1).toLong, m.apply(2).toLong))
  i.next()
  val humidityToLocation = i.takeWhile(mapRegex.matches(_)).toList.map(_.split(" ")).map(m => List(m.apply(0).toLong, m.apply(1).toLong, m.apply(2).toLong))
  new Almanac(seeds,seedsToSoil,soilToFertilizer,fertilizerToWater,waterToLight,lightToTemperature,temperatureToHumidity,humidityToLocation)
} 

def sectionMap(from: List[Long], to: List[List[Long]]): List[Long] = { 
  val mappings =  for 
                    f <- from
                  yield
                    for 
                      t <- to
                    yield
                      t match {
                        case List(dest, source, range) if f >= source && f <= source +range -1 => Option(dest + f-source)
                        case _ => Option.empty
                      }
  mappings.flatten.filter(_.nonEmpty).map(_.get)
}

def part1(almanac: Almanac): Long = {
  val seeds = almanac.seeds

  val soils = sectionMap(seeds, almanac.seedsToSoil)
  val fertilizer = sectionMap(soils, almanac.soilToFertilizer)
  val water = sectionMap(fertilizer, almanac.fertilizerToWater)
  val light = sectionMap(water, almanac.waterToLight)
  val temperature = sectionMap(light, almanac.lightToTemperature)
  val humidities = sectionMap(temperature, almanac.temperatureToHumidity)
  val locations = sectionMap(humidities, almanac.humidityToLocation)
  println(locations)
  
  return 0l
  /*val locations = almanac.humidityToLocation.map(m => m(0) to m(0)+m(2)-1)
  println(s"Locations: $locations")
  {for 
    location <- locations
  yield {
    val humidities = sectionMap(location.toList.map(k => (k,k)), almanac.humidityToLocation)
    println(s"Humidities: $humidities")
    val temperatures = sectionMap(humidities, almanac.temperatureToHumidity)
    println(s"Temperaturs: $temperatures")
    val lights = sectionMap(temperatures, almanac.lightToTemperature)
    println(s"Lights: $lights")
    val waters = sectionMap(lights, almanac.waterToLight)
    println(s"Waters: $waters")
    val fertilizers = sectionMap(waters, almanac.fertilizerToWater)
    print(s"Fertilizers: $fertilizers")
    val soils = sectionMap(fertilizers, almanac.soilToFertilizer)
    println(s"Soils: $soils")
    val seeds = sectionMap(soils, almanac.seedsToSoil)
    println(s"Seeds: $seeds")
    seeds.sortBy(_._2).head._2
  }}.sorted.head*/
}

def solve : Unit = {
  val filename = "data/day05-input"
  val lines = Source.fromFile(filename).getLines().toList
  val almanac = parseAlmanac(lines)
  println("__Day 5__")
  println(s"Part 1: ${part1(almanac)}")
}
