import parse
from behave import step, register_type, use_step_matcher
from behave.runner import Context
from pyassert import assert_that

use_step_matcher("parse")


@parse.with_pattern(r'\d+')
def parse_integer(text: int):
    return int(text)


register_type(Integer=parse_integer)


@step("APIサーバにリクエストする")
def step_impl(context: Context) -> None:
    """
    :type context: behave.runner.Context
    """
    # ステータスコードのステップを実行したいので、一旦無視する
    pass


# status_codeがstrでないという警告が出るので無効化する
# noinspection PyBDDParameters
@step("ステータスコードが {status_code:Integer} である")
def step_impl(context: Context, status_code: int) -> None:
    """
    :type context: behave.runner.Context
    :type status_code: int
    """
    # intに変換されていることを確認する
    assert_that(status_code).is_instance_of(int)
