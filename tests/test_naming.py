from tcepepy.naming import clean_name, clean_names


def test_camel_case():
    assert clean_name("CodigoEfiscoUG") == "codigo_efisco_ug"


def test_existing_underscores():
    assert clean_name("ID_UNIDADE_GESTORA") == "id_unidade_gestora"


def test_all_caps_no_boundary():
    assert clean_name("CATEGORIARECEITA") == "categoriareceita"


def test_accents_folded():
    assert clean_name("Município") == "municipio"
    assert clean_name("Razão Social") == "razao_social"


def test_leading_digit_prefixed():
    assert clean_name("123abc") == "x123abc"


def test_empty_becomes_x():
    assert clean_name("---") == "x"


def test_duplicates_disambiguated():
    assert clean_names(["Valor", "VALOR", "valor"]) == ["valor", "valor_2", "valor_3"]
