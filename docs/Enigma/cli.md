<!-- @format -->

# Cli

> Auto-generated documentation for [Enigma.cli](blob/master/Enigma/cli.py) module.

-   [Enigma machine](..\README.md#enigma-machine-python) / [Modules](..\MODULES.md#enigma-machine-modules) / [Enigma](index.md#enigma) / Cli
    -   [main](#main)
    -   [verifRots](#verifrots)

## main

[[find in source code]](blob/master/Enigma/cli.py#L28)

```python
@click.command()
@click.option(
    '-e/-d',
    '--encipher/--decipher',
    is_flag=True,
    default=True,
    help='Whether to encrypt or decrypt the string',
)
@click.option(
    '-s',
    '--starting-position',
    default=['A', 'A', 'A'],
    show_default=True,
    type=click.Choice(ascii_uppercase, False),
    nargs=3,
    help='Rotors starting position',
    callback=lambda ctx, param, value: [char.upper() for char in value],
)
@click.option(
    '-r',
    '--rotors',
    default=['1', '2', '3'],
    show_default=True,
    type=str,
    multiple=True,
    callback=verifRots,
    help=' Rotor to be used',
)
@click.option(
    '-rf',
    '--reflector',
    default='B',
    show_default=True,
    type=str,
    help='Reflector to be used',
)
@click.option(
    '-rs',
    '--ring-setting',
    default=['A', 'A', 'A'],
    show_default=True,
    type=click.Choice(ascii_uppercase, False),
    nargs=3,
    help='Rotors ring setting',
)
@click.option(
    '-p',
    '--plugboard',
    default=[
        ('P', 'O'),
        ('M', 'L'),
        ('I', 'U'),
        ('K', 'J'),
        ('N', 'H'),
        ('Y', 'T'),
        ('G', 'B'),
        ('V', 'F'),
        ('R', 'E'),
        ('D', 'C'),
    ],
    show_default=True,
    type=click.Choice(ascii_uppercase, False),
    nargs=2,
    multiple=True,
    callback=lambda ctx, param, value: [(c1.upper(), c2.upper()) for (c1, c2) in value],
    help='Plugboard configuration',
)
@click.option(
    '-n',
    '--encrypt-num',
    is_flag=False,
    flag_value='1',
    default='0',
    show_default=True,
    type=click.Choice(['0', '1', '2']),
    callback=lambda ctx, param, value: int(value),
    help='Ignore (0), Encrypted (1) or Remove (2) numbers',
)
@click.option(
    '-c',
    '--encrypt-capital',
    is_flag=False,
    flag_value='1',
    default='0',
    show_default=True,
    type=click.Choice(['0', '1']),
    callback=lambda ctx, param, value: int(value),
    help='Ignore (0), Encrypted (1) or Remove (2) capitals',
)
@click.option(
    '-sp',
    '--encrypt-special',
    is_flag=False,
    flag_value='1',
    default='0',
    show_default=True,
    type=click.Choice(['0', '1', '2']),
    callback=lambda ctx, param, value: int(value),
    help='Ignore (0), Encrypted (1) or Remove (2) special',
)
@click.option(
    '-w',
    '--encrypt-whitespace',
    is_flag=False,
    flag_value='1',
    default='0',
    show_default=True,
    type=click.Choice(['0', '1', '2']),
    callback=lambda ctx, param, value: int(value),
    help='Ignore (0), Encrypted (1) or Remove (2) whitespace',
)
@click.option(
    '-cr',
    '--custom-rotor',
    nargs=3,
    type=str,
    is_eager=True,
    callback=lambda ctx, param, value: storage.addCustomRotor(*value) if value is not None else None,
    help='Adds custom rotor takes the rotor-ID,keys, notch as arguments to create a custom rotor',
)
@click.option(
    '-cf',
    '--custom-reflector',
    nargs=2,
    type=str,
    is_eager=True,
    callback=lambda ctx, param, value: storage.addCustomReflector(*value) if value is not None else None,
    help='Adds custom reflector takes the reflector-ID and keys as arguments to create a custom reflector',
)
@click.argument('string')
def main(
    encipher,
    starting_position,
    rotors,
    reflector,
    ring_setting,
    plugboard,
    encrypt_num,
    encrypt_capital,
    encrypt_special,
    encrypt_whitespace,
    custom_rotor,
    custom_reflector,
    string,
):
```

## verifRots

[[find in source code]](blob/master/Enigma/cli.py#L10)

```python
def verifRots(ctx, param, value):
```
