import main.scala.day06._

class Day6_Tests extends munit.FunSuite {

  test("Find Range 1") {
    val obtained = findRange(7, 9)
    val expected = (2.toLong, 5.toLong)
    assertEquals(obtained, expected)
  }

  test("Find Range 2") {
    val obtained = findRange(15,40)
    val expected = (4.toLong, 11.toLong)
    assertEquals(obtained, expected)
  }

    test("Find Range 3") {
    val obtained = findRange(30, 200)
    val expected = (11.toLong, 19.toLong)
    assertEquals(obtained, expected)
  }


  test("Test Full Part 1") {
    val records = List(
      "Time:      7  15   30",
      "Distance:  9  40  200").iterator

    val intRegex = """\d+""".r
    val times = intRegex.findAllMatchIn(records.next()).map(_.group(0).toLong)
    val distances = intRegex.findAllMatchIn(records.next()).map(_.group(0).toLong)
    val expected = 288.toLong
    val obtained = (times zip distances).map((t:Long, d:Long) => findRange(t,d)).map((r) => r._2 - r._1 +1).reduce(_ * _)
    assertEquals(obtained, expected)
  }

  test("Full Part 2 Test") {
    val records = List(
      "Time:      7  15   30",
      "Distance:  9  40  200").iterator

    val intRegex = """\d+""".r
    val time = intRegex.findAllMatchIn(records.next()).map(_.group(0)).reduce(_+_).toLong
    val distance = intRegex.findAllMatchIn(records.next()).map(_.group(0)).reduce(_+_).toLong
    val expected = 71503.toLong
    val range = findRange(time, distance)
    val obtained = range._2 - range._1 + 1
    assertEquals(obtained, expected)
  }
}
