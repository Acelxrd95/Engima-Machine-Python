import click
from string import ascii_uppercase
from enigma import Enigma
import storage
import sys

sys.tracebacklimit = 0


def verifRots(ctx, param, value):
    if len(value) < 3:
        value = list(value)
        defaults = ["1", "2", "3"]
        for i in range(3):
            try:
                if value[i] in storage.rotors.keys():
                    pass
                else:
                    raise KeyError(f"Rotor key {value[i]} not a valid rotor ID")
            except IndexError:
                value.append(defaults[i])
    if len(value) == 3:
        return tuple(value)
    if len(value) > 3:
        raise click.ClickException(f"Only 3 rotor values allowed not {len(value)}")


@click.command()
@click.option(
    "-e/-d",
    "--encipher/--decipher",
    is_flag=True,
    default=True,
    help="Whether to encrypt or decrypt the string",
)
@click.option(
    "-s",
    "--start-position",
    default=["A", "A", "A"],
    show_default=True,
    type=click.Choice(ascii_uppercase, False),
    nargs=3,
    help="Rotors starting position",
    callback=lambda ctx, param, value: [char.upper() for char in value],
)
@click.option(
    "-r",
    "--rotors",
    default=["1", "2", "3"],
    show_default=True,
    type=str,
    multiple=True,
    callback=verifRots,
    help=" Rotor to be used",
)
@click.option(
    "-rf",
    "--reflector",
    default="B",
    show_default=True,
    type=str,
    help="Reflector to be used",
)
@click.option(
    "-rs",
    "--ring-setting",
    default=["A", "A", "A"],
    show_default=True,
    type=click.Choice(ascii_uppercase, False),
    nargs=3,
    help="Rotors ring setting",
)
@click.option(
    "-p",
    "--plugboard",
    default=[
        ("P", "O"),
        ("M", "L"),
        ("I", "U"),
        ("K", "J"),
        ("N", "H"),
        ("Y", "T"),
        ("G", "B"),
        ("V", "F"),
        ("R", "E"),
        ("D", "C"),
    ],
    show_default=True,
    type=click.Choice(ascii_uppercase, False),
    nargs=2,
    multiple=True,
    callback=lambda ctx, param, value: [(c1.upper(), c2.upper()) for c1, c2 in value],
    help="Plugboard configuration",
)
@click.option(
    "-n",
    "--encrypt-num",
    is_flag=False,
    flag_value="1",
    default="0",
    show_default=True,
    type=click.Choice(["0", "1", "2"]),
    callback=lambda ctx, param, value: int(value),
    help="Ignore (0), Encrypted (1) or Remove (2) numbers",
)
@click.option(
    "-c",
    "--encrypt-capital",
    is_flag=False,
    flag_value="1",
    default="0",
    show_default=True,
    type=click.Choice(["0", "1"]),
    callback=lambda ctx, param, value: int(value),
    help="Ignore (0), Encrypted (1) or Remove (2) capitals",
)
@click.option(
    "-sp",
    "--encrypt-special",
    is_flag=False,
    flag_value="1",
    default="0",
    show_default=True,
    type=click.Choice(["0", "1", "2"]),
    callback=lambda ctx, param, value: int(value),
    help="Ignore (0), Encrypted (1) or Remove (2) special",
)
@click.option(
    "-w",
    "--encrypt-whitespace",
    is_flag=False,
    flag_value="1",
    default="0",
    show_default=True,
    type=click.Choice(["0", "1", "2"]),
    callback=lambda ctx, param, value: int(value),
    help="Ignore (0), Encrypted (1) or Remove (2) whitespace",
)
@click.option(
    "-cr",
    "--custom-rotor",
    nargs=3,
    type=str,
    is_eager=True,
    callback=lambda ctx, param, value: storage.addCustomRotor(*value)
    if value is not None
    else None,
    help="Adds custom rotor takes the rotor-ID,keys, notch as arguments to create a custom rotor",
)
@click.option(
    "-cf",
    "--custom-reflector",
    nargs=2,
    type=str,
    is_eager=True,
    callback=lambda ctx, param, value: storage.addCustomReflector(*value)
    if value is not None
    else None,
    help="Adds custom reflector takes the reflector-ID and keys as arguments to create a custom reflector",
)
@click.argument("string")
def main(
    encipher,
    start_position,
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
    mach = Enigma(
        start_position,
        rotors,
        reflector,
        ring_setting,
        plugboard,
        encrypt_num,
        encrypt_capital,
        encrypt_special,
        encrypt_whitespace,
    )
    if encipher:
        click.echo(mach.encipher(string))
    else:
        click.echo(mach.decipher(string))


if __name__ == "__main__":
    main()
