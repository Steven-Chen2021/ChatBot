import importlib

pe = importlib.import_module('backend_api.prompt_engine')


def test_build_prompt_with_context():
    pe.set_system_prompt('SYSTEM')
    prompt = pe.build_prompt('hello', context='info')
    assert 'SYSTEM' in prompt
    assert 'Context:\ninfo' in prompt
    assert prompt.strip().endswith('User: hello')


def test_set_system_prompt_affects_build():
    pe.set_system_prompt('NEW PROMPT')
    assert pe.build_prompt('x').splitlines()[0] == 'NEW PROMPT'
