import pytest

def apply_discounts(cart_total, discount_codes):
    valid_discounts = {'SAVE10': 0.10, 'SAVE20': 0.20, 'SAVE50': 0.50}
    total_discount = 0
    for code in discount_codes:
        if code not in valid_discounts:
            raise ValueError(f"Invalid discount code: {code}")
        if total_discount + valid_discounts[code] > 1:
            raise ValueError("Total discount cannot exceed 100%.")
        total_discount += valid_discounts[code]
    return cart_total * (1 - total_discount)


###Test-Case-01
@pytest.mark.parametrize(
    "cart_total, discount_codes, expected_total",
    [
        #with single code
        pytest.param(100, ["SAVE10"], 90.0, id="single_code_10_percent"),

        #multiple valid codes_01
        pytest.param(200, ["SAVE50", "SAVE20"], 60.0, id="multiple_valid_codes_01"),

        #multiple valid codes_02
        pytest.param(150, ["SAVE10", "SAVE20"], 105.0, id="multiple_valid_codes_02"),

        #multiple valid codes_03
        pytest.param(150, ["SAVE20", "SAVE20"], 90.0, id="multiple_valid_codes_03"),

        #multiple valid codes_04
        pytest.param(200, ["SAVE10", "SAVE10", "SAVE20", "SAVE50"], 20.0, id="multiple_valid_codes_04"),

        #multiple valid codes_05
        pytest.param(100, ["SAVE10", "SAVE10", "SAVE10", "SAVE10", "SAVE10", "SAVE10",
                           "SAVE10", "SAVE10", "SAVE10", "SAVE10"], 
                           0.0, id="multiple_valid_codes_05"),
        
        #multiple valid codes_06
        pytest.param(100, ["SAVE20", "SAVE20", "SAVE20", "SAVE20", "SAVE20"], 
                           0.0, id="multiple_valid_codes_06"),
        
        #multiple valid codes_07
        pytest.param(100, ["SAVE50", "SAVE50"], 0.0, id="multiple_valid_codes_07"),

        #multiple valid codes_08
        pytest.param(100, ["SAVE50", "SAVE20", "SAVE20", "SAVE10"], 0.0, id="multiple_valid_codes_08"),

        #multiple valid codes_09
        pytest.param(101, ["SAVE50", "SAVE20", "SAVE10", "SAVE10"], 10.1, id="multiple_valid_codes_09"),

        #empty discount list
        pytest.param(150, [], 150.0, id="no_discount"),
    ],
)
def test_apply_discounts_normal_cases(cart_total, discount_codes, expected_total):
    result = apply_discounts(cart_total, discount_codes)
    assert result == pytest.approx(expected_total), (
        f"Cart Total: {cart_total}," 
        f"Discount Codes: {discount_codes}," 
        f"Expected Total: {expected_total}," 
        f"Result: {result}"
    )
    print(f"Assertion OK ✅: Cart Total: {cart_total}, Discount Codes: {discount_codes}, Expected Total: {expected_total}, Actual Result: {result}")


###Test-Case-02
@pytest.mark.parametrize(
    "cart_total, discount_codes, expected_total",
    [
        #single code with float cart
        pytest.param(99.99, ["SAVE10"], 89.991, id="float_cart_single"),

        #multiple codes with float cart
        pytest.param(149.75, ["SAVE10", "SAVE20"], 104.825, id="float_cart_with_multiple_codes-01"),

        #high cart value
        pytest.param(257.30, ["SAVE50"], 128.65, id="float_cart_with_half_discount"),

        #boundary exactly 100%
        pytest.param(120.40, ["SAVE50", "SAVE50"], 0.0, id="float_cart_with_exact_100_percent_discount"),

        #many small discounts
        pytest.param(199.99, ["SAVE10", "SAVE10", "SAVE20"], 119.994, id="float_cart_with_multiple_codes-02"),
    ],
)
def test_apply_discounts_float_cases(cart_total, discount_codes, expected_total):
    result = apply_discounts(cart_total, discount_codes)
    assert result == pytest.approx(expected_total), (
        f"Cart Total: {cart_total}," 
        f"Discount Codes: {discount_codes}," 
        f"Expected Total: {expected_total}," 
        f"Result: {result}"
    )
    print(f"Assertion OK ✅: Cart Total: {cart_total}, Discount Codes: {discount_codes}, Expected Total: {expected_total}, Actual Result: {result}")


###Test-Case-03
@pytest.mark.parametrize(
    "cart_total, discount_codes",
    [
        #invalid discount code
        pytest.param(100, ["ABC"], id="invalid_single_code"),
        pytest.param(200, ["INVALID", "SAVE50"], id="invalid_first_code"),
        pytest.param(200, ["SAVE10", "INVALID"], id="invalid_second_code"),
        pytest.param(200, ["INVALID", "INVALID"], id="invalid_both_code"),
    ],
)
def test_apply_discounts_invalid_code(cart_total, discount_codes):
    with pytest.raises(ValueError) as e:
        apply_discounts(cart_total, discount_codes)

    msg = str(e.value)
    assert "Invalid discount code:" in msg
    print("Assertion:", msg)


###Test-Case-04
@pytest.mark.parametrize(
    "cart_total, discount_codes",
    [
        #exceed 100 percent_01
        pytest.param(100, ["SAVE50", "SAVE50", "SAVE10"], id="exceed_100_percent_01"),

        #exceed 100 percent_02
        pytest.param(100, ["SAVE10", "SAVE10", "SAVE10", "SAVE10", "SAVE10", "SAVE10",
                           "SAVE10", "SAVE10", "SAVE10", "SAVE10", "SAVE10"],
                           id="exceed_100_percent_02"),
        
        #exceed 100 percent_03
        pytest.param(100, ["SAVE20", "SAVE20", "SAVE20", "SAVE20", "SAVE20", "SAVE20"],
                           id="exceed_100_percent_03"),
        
        #exceed 100 percent_04
        pytest.param(100, ["SAVE50", "SAVE50", "SAVE10"], id="exceed_100_percent_04"),

        #exceed 100 percent_05
        pytest.param(100, ["SAVE50", "SAVE20", "SAVE20", "SAVE10" , "SAVE10"], id="exceed_100_percent_05"),
    ],
)
def test_apply_discounts_exceed_100_percent(cart_total, discount_codes):
    with pytest.raises(ValueError) as e:
        apply_discounts(cart_total, discount_codes)
    
    msg = str(e.value)
    assert "Total discount cannot exceed 100%" in msg
    print("Assertion:", msg)