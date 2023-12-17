import main.scala.day9._
import scala.compiletime.ops.int

class Day9_Tests extends munit.FunSuite {
    test("Calculate Next Row 1"){
        val intRegex = """\d+""".r
        val row = "0 3 6 9 12 15"
        val ints = intRegex.findAllMatchIn(row).map(_.group(0).toLong).toList
        val obtained = nextRow(ints)
        val expected = List[Long](3, 3, 3, 3, 3)
        assertEquals(obtained, expected)
    }   

    test("Calculate Next Row 2"){
        val intRegex = """\d+""".r
        val row = "3   3   3   3   3"
        val ints = intRegex.findAllMatchIn(row).map(_.group(0).toLong).toList
        val obtained = nextRow(ints)
        val expected = List[Long](0, 0, 0, 0)
        assertEquals(obtained, expected)
    }   

    test("Calculate Next Row 3"){
        val intRegex = """\d+""".r
        val row = "1 3 6 10 15 21"
        val ints = intRegex.findAllMatchIn(row).map(_.group(0).toLong).toList
        val obtained = nextRow(ints)
        val expected = List[Long](2, 3, 4, 5, 6)
        assertEquals(obtained, expected)
    }   

    test("Next Value Test 1") {
        val intRegex = """\d+""".r
        val row = "0 3 6 9 12 15"
        val ints = intRegex.findAllMatchIn(row).map(_.group(0).toLong).toList
        val obtained = nextValue(ints)
        val expected = 18.toLong
        assertEquals(obtained, expected)
    }

    test("Next Value Test 2") {
        val intRegex = """\d+""".r
        val row = "1 3 6 10 15 21"
        val ints = intRegex.findAllMatchIn(row).map(_.group(0).toLong).toList
        val obtained = nextValue(ints)
        val expected = 28l
        assertEquals(obtained, expected)
    }

    test("Next Value Test 3") {
        val intRegex = """\d+""".r
        val row = "10 13 16 21 30 45"
        val ints = intRegex.findAllMatchIn(row).map(_.group(0).toLong).toList
        val obtained = nextValue(ints)
        val expected = 68l
        assertEquals(obtained, expected)
    }

    test("Full Part 1 Test") {
        val intRegex = """-?\d+""".r
        val lines = List(
            "0 3 6 9 12 15",
            "1 3 6 10 15 21",
            "10 13 16 21 30 45"
        )
        val expected = 114l
        val obtained = lines.map(intRegex.findAllMatchIn(_).map(_.group(0).toLong).toList).map(nextValue(_)).reduce(_+_)
        assertEquals(obtained, expected)
    }

    test("Previous Value Test 1") {
        val intRegex = """\d+""".r
        val row = "0 3 6 9 12 15"
        val ints = intRegex.findAllMatchIn(row).map(_.group(0).toLong).toList
        val obtained = previousValue(ints)
        val expected = -3l
        assertEquals(obtained, expected)
    }

    test("Previous Value Test 2") {
        val intRegex = """\d+""".r
        val row = "1 3 6 10 15 21"
        val ints = intRegex.findAllMatchIn(row).map(_.group(0).toLong).toList
        val obtained = previousValue(ints)
        val expected = 0l
        assertEquals(obtained, expected)
    }

    test("Previous Value Test 3") {
        val intRegex = """\d+""".r
        val row = "10 13 16 21 30 45"
        val ints = intRegex.findAllMatchIn(row).map(_.group(0).toLong).toList
        val obtained = previousValue(ints)
        val expected = 5l
        assertEquals(obtained, expected)
    }

    test("Previous Value Test 4") {
        val intRegex = """-?\d+""".r
        val row = "-2 -7 -12 -17 -22 -27 -32 -37 -42 -47 -52 -57 -62 -67 -72 -77 -82 -87 -92 -97"
        val expected = 3l

        val ints = intRegex.findAllMatchIn(row).map(_.group(0).toLong).toList
        val obtained = previousValue(ints)
        assertEquals(obtained, expected)
    }

    test("Full Part 2 Test") {
        val intRegex = """-?\d+""".r
        val lines = List(
            "0 3 6 9 12 15",
            "1 3 6 10 15 21",
            "10 13 16 21 30 45"
        )
        val expected = 2l
        val obtained = lines.map(intRegex.findAllMatchIn(_).map(_.group(0).toLong).toList).map(previousValue(_)).reduce(_+_)
        assertEquals(obtained, expected)
    }
}