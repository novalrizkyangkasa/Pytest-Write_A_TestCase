import pytest

def validate_shipping_address(address):
    required_fields = ['name', 'street', 'city', 'postcode', 'country']
    if not isinstance(address, dict):
        raise ValueError("Address must be a dictionary.")
    
    missing_fields = [field for field in required_fields if field not in address]
    if missing_fields:
        raise ValueError(f"Missing required fields: {','.join(missing_fields)}")
    
    return True


###Test-Case-01
@pytest.mark.parametrize(
    "address",
    [
        #valid address
        pytest.param(
        {
            "name": "John Doe",
            "street": "Jl. Sudirman",
            "city": "Malang",
            "postcode": "65122",
            "country": "Indonesia",
        },
        id="valid_address",
        ),
    ],
)
def test_validate_shipping_address_valid(address):
    assert validate_shipping_address(address) is True
    print(f"Assertion OK ✅: Address is valid:", address)


###Test-Case-02
def test_validate_shipping_address_invalid_type():

    #invalid type with List
    address = [
        "John Doe",
        "Jl. Sudirman",
        "Malang",
        "65122",
        "Indonesia",
    ]

    with pytest.raises(ValueError) as e:
        validate_shipping_address(address)
    assert str(e.value) == "Address must be a dictionary."
    print("Error message:", e.value)


###Test-Case-03
@pytest.mark.parametrize(
    "address, expected_missing",
    [
        #missing fields "name"
        pytest.param(
            {
                "street": "Jl. Sudirman",
                "city": "Malang",
                "postcode": "65122",
                "country": "Indonesia",
            },
            ["name"],
            id="missing_name",
        ),

       #missing fields "street"
        pytest.param(
            {
                "name": "John Doe",
                "city": "Malang",
                "postcode": "65122",
                "country": "Indonesia",
            },
            ["street"],
            id="missing_street",
        ),

        #missing fields "city"
        pytest.param(
            {
                "name": "John Doe",
                "street": "Jl. Sudirman",
                "postcode": "65122",
                "country": "Indonesia",
            },
            ["city"],
            id="missing_city",
        ),

        #missing fields "postcode"
        pytest.param(
            {
                "name": "John Doe",
                "street": "Jl. Sudirman",
                "city": "Malang",
                "country": "Indonesia",
            },
            ["postcode"],
            id="missing_postcode",
        ),

        #missing fields "country"
        pytest.param(
            {
                "name": "John Doe",
                "street": "Jl. Sudirman",
                "city": "Malang",
                "postcode": "65122",
            },
            ["country"],
            id="missing_country",
        ),

        #missing multiple fields
        pytest.param(
            {
                "street": "Jl. Sudirman",
                "city": "Malang",
            },
            ["name", "postcode", "country"],
            id="missing_multiple_fields",
        ),

        #missing all fields
        pytest.param(
            {},
            ["name", "street", "city", "postcode", "country"],
            id="missing_all_fields",
        ),
    ],
)
def test_validate_shipping_address_missing_fields(address, expected_missing):
    with pytest.raises(ValueError) as e:
        validate_shipping_address(address)

    msg = str(e.value)
    assert msg.startswith("Missing required fields:")

    for field in expected_missing:
        assert field in msg
    print("Assertion:", msg)