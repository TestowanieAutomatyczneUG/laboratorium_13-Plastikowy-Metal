from pytest_bdd import scenario, given, when, then
from behave import *
from pangram import Pangram


@given("there is a object Pangram")
def step_impl(context):
    context.temp = Pangram()


@when('string is "{string}"')
def step_impl(context, string):
    context.result = context.temp.is_pangram(string)


@then('function returns "{r}"')
def step_impl(context, r):
    print(r)
    print(context.result)
    assert str(context.result) == r

