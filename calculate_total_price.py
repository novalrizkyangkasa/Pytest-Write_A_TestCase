import pytest

def calculate_cart_total(cart_items, discount=0):
    if not isinstance(cart_items, list) or not all(isinstance(item, dict) for item in cart_items):
        raise ValueError("Cart items should be a list of dictionaries.")
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    return total * (1 - discount)


###Test-Case-01
@pytest.mark.parametrize(
    "cart_items, discount, expected_total",
    [
        #empty cart
        pytest.param([], 0.0, 0.0, id="empty_cart_no_discount"),
        pytest.param([], 0.5, 0.0, id="empty_cart_with_discount"),

        #single item, no discount
        pytest.param([{"price": 10, "quantity": 1}], 0.0, 10.0, id="single_item_no_discount"),

        #multiple items, no discount
        pytest.param([{"price": 10, "quantity": 1}, {"price": 20, "quantity": 2}], 0.0, 50.0, id="multiple_items_no_discount"),

        #discount applied with single item
        pytest.param([{"price": 10, "quantity": 1}], 0.5, 5.0, id="single_item_with_discount"),

        #discount applied with multiple items
        pytest.param([{"price": 10, "quantity": 1}, {"price": 20, "quantity": 2}], 0.5, 25.0, id="multiple_items_with_discount"),

        #discount applied with full discount
        pytest.param([{"price": 10, "quantity": 1}, {"price": 20, "quantity": 2}], 1.0, 0.0, id="full_discount"),
    ],
)
def test_calculate_cart_total_valid(cart_items, discount, expected_total):
    result = calculate_cart_total(cart_items, discount)
    assert result == pytest.approx(expected_total)
    print(f"Assertion OK ✅: Cart items: {cart_items}, Discount: {discount}, Expected Total: {expected_total}, Actual Result: {result}")


###Test-Case-02
@pytest.mark.parametrize(
    "cart_items, discount, expected_total",
    [
        #decimal discount
        pytest.param([{"price": 10, "quantity": 1}], 0.33, 6.7, id="float_discount"),

        #decimal price
        pytest.param([{"price": 9.99, "quantity": 2}], 0.10, 17.982, id="float_price_with_discount"),

        #multiple items with decimal result
        pytest.param([{"price": 15.15, "quantity": 1}, {"price": 7.7, "quantity": 3}], 0.15, 32.5125, id="multiple_items_float_discount"),
    ],
)
def test_calculate_cart_total_float_cases(cart_items, discount, expected_total):
    result = calculate_cart_total(cart_items, discount)
    assert result == pytest.approx(expected_total)
    print(f"Assertion OK ✅: Cart items: {cart_items}, Discount: {discount}, Expected Total: {expected_total}, Actual Result: {result}")


###Test-Case-03
@pytest.mark.parametrize(
    "cart_items",
    [
        #invalid cart items
        pytest.param("not a list", id="string_input"),
        pytest.param(123, id="integer_input"),
        pytest.param(None, id="none_input"),
        pytest.param({"price": "10", "quantity": 1}, id="list_not_listed"),
        pytest.param(["price", 10, "quantity", 1], id="dict_not_listed"),
        pytest.param([{"price": 10, "quantity": 1}, "not have amount"], id="mixed_types"),
    ],
)
def test_invalid_structure_raises_value_error(cart_items):
    with pytest.raises(ValueError) as e:
        calculate_cart_total(cart_items)
    assert str(e.value) == "Cart items should be a list of dictionaries."
    print("Error message:", e.value)


###Test-Case-04
@pytest.mark.parametrize(
    "cart_items",
    [
        #missing quantity
        pytest.param([{"price": 10}], id="missing_quantity"),
        
        #missing price
        pytest.param([{"quantity": 1}], id="missing_price"),

        #missing one item key
        pytest.param([{"price": 10, "quantity": 1}, {"price": 20}], id="missing_quantity_item_key_in_second_item"),
        pytest.param([{"price": 10, "quantity": 1}, {"quantity": 2}], id="missing_price_item_key_in_second_item"),
        pytest.param([{"price": 10}, {"price": 20, "quantity": 2}], id="missing_quantity_item_key_in_first_item"),
        pytest.param([{"quantity": 10}, {"price": 20, "quantity": 2}], id="missing_price_item_key_in_first_item"),
    ],
)
def test_calculate_cart_total_missing_keys(cart_items):
    # function doesn't validate keys, so KeyError is expected
    with pytest.raises(KeyError) as e:
        calculate_cart_total(cart_items)
    print(e.value)


###Test-Case-05
@pytest.mark.parametrize(
    "cart_items",
    [
        #string price -> TypeError during calculation
        pytest.param([{"price": "100", "quantity": 2}], id="string_price"),

        #string quantity -> TypeError during calculation 
        pytest.param([{"price": 100, "quantity": "2"}], id="string_quantity"),

        #string price -> TypeError during calculation
        pytest.param([{"price": "one hundred", "quantity": 2}], id="string_price_with_non_numeric_values"),

        #string quantity -> TypeError during calculation 
        pytest.param([{"price": 100, "quantity": "two"}], id="string_quantity_with_non_numeric_values"),
    ],
)
def test_calculate_cart_total_non_numeric_values(cart_items):
    with pytest.raises(TypeError) as e:
        calculate_cart_total(cart_items)
    print(e.value)


###Test-Case-06
def test_calculate_cart_total_default_discount():

    #verify default discount
    cart_items = [{"price": 100, "quantity": 2}]
    result = calculate_cart_total(cart_items)
    assert result == 200
