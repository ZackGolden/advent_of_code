import main.scala.day6._

class Day6_Tests extends munit.FunSuite {
  test("example test that succeeds") {
    val obtained = 42
    val expected = 42
    assertEquals(obtained, expected)
  }

  test("Find Range 1") {
    val obtained = findRange(7, 9)
    val expected = (2, 5)
    assertEquals(obtained, expected)
  }

  test("Find Range 2") {
    val obtained = findRange(15,40)
    val expected = (4, 11)
    assertEquals(obtained, expected)
  }

    test("Find Range 3") {
    val obtained = findRange(30, 200)
    val expected = (11, 19)
    assertEquals(obtained, expected)
  }


  test("Test Full Part 1") {
    val records = List(
      "Time:      7  15   30",
      "Distance:  9  40  200")
    val expected = 288
    val obtained = 12
    assertEquals(obtained, expected)
  }
}