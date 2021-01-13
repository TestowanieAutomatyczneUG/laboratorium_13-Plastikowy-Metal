from pytest_bdd import scenario, given, when, then
from assertpy import *
from behave import *
from main import FizzBuzz


@given("I create FizzBuzz class")
def step_impl(context):
    context.temp = FizzBuzz()


@when("I call method game with argument equal 15")
def step_impl(context):
    context.game = context.temp.game(15)


@then("I should get result FizzBuzz")
def step_impl(context):
    assert context.game == "FizzBuzz"


@when("I call method game with argument equal 5")
def step_impl(context):
    context.game2 = context.temp.game(5)


@then("I should get result Buzz")
def step_impl(context):
    assert context.game2 == "Buzz"


@when("I call method game with argument equal 3")
def step_impl(context):
    context.game3 = context.temp.game(3)


@then("I should get result Fizz")
def step_impl(context):
    assert context.game3 == "Fizz"


@when("I call method game with argument equal 7")
def step_impl(context):
    context.game = context.temp.game(7)


@then("I should get result Not fizz not buzz not fizzbuzz")
def step_impl(context):
    assert context.game == "Not fizz not buzz not fizzbuzz"


@when("I call method game with argument equal -7")
def step_impl(context):
    context.game = context.temp.game(-7)