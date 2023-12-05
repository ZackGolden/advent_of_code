import main.scala.day3._

class Day3_Tests extends munit.FunSuite {


  test("Test Find Symbols") {
    val schematic = List(
      "467..114..",
      "...*......",
      "..35..633.",
      "......#...",
      "617*......",
      ".....+.58.",
      "..592.....",
      "......755.",
      "...$.*....",
      ".664.598..",
    )
    val expected = List(
      "3,1",
      "6,3",
      "3,4",
      "5,5",
      "3,8",
      "5,8"
    ).sorted
    val obtained = findSymbols(schematic).sorted
    assertEquals(obtained, expected)
  }

  test("Test Sweep True 1") {
    val numberRegex = """[\d]+""".r
    val symbols = List(
      "3,1",
      "6,3",
      "3,4",
      "5,5",
      "3,8",
      "5,8"
    )
    for 
      part <- numberRegex.findAllMatchIn("467..114..")
    do
      println(sweep(part, 0, symbols.toSet))

  }

  test("Full Part 1 Test") {
    val schematic = List(
      "467..114..",
      "...*......",
      "..35..633.",
      "......#...",
      "617*......",
      ".....+.58.",
      "..592.....",
      "......755.",
      "...$.*....",
      ".664.598..",
    )
    val obtained = findAdjacentComponents(schematic)
    val expected = 4361
    assertEquals(obtained, expected)
  }
  
  test("Test Find Gears") {
    val schematic = List(
      "467..114..",
      "...*......",
      "..35..633.",
      "......#...",
      "617*......",
      ".....+.58.",
      "..592.....",
      "......755.",
      "...$.*....",
      ".664.598..",
    )
    val expected = List(
      "3,1",
      "3,4",
      "5,8"
    ).sorted
    val obtained = findGears(schematic).sorted
    assertEquals(obtained, expected)
  }

  test("Test Part 2 Full Run") {
    val schematic = List(
      "467..114..",
      "...*......",
      "..35..633.",
      "......#...",
      "617*......",
      ".....+.58.",
      "..592.....",
      "......755.",
      "...$.*....",
      ".664.598..",
    )
    val expected = 467835
    val obtained = createListOfAdjacentComponents(schematic).filter(_._2.size==2).map(_._2.reduce(_*_)).reduce(_+_)
    assertEquals(obtained, expected)
  }
}
