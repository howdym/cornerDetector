import utils
import cv2

top = cv2.imread("top.png", cv2.IMREAD_COLOR)
bottom = cv2.imread("bottom.png", cv2.IMREAD_COLOR)
notPage = cv2.imread("notPage.png", cv2.IMREAD_COLOR)
moving = cv2.imread("moving.png", cv2.IMREAD_COLOR)
moving2 = cv2.imread("moving2.png", cv2.IMREAD_COLOR)

# Test case 1: Test target page with itself
assert utils.confirm_page(top)

# Test case 2: Test target page with non-target page
assert not utils.confirm_page(notPage)

# Test case 3: Test target page with another target page
assert utils.confirm_page(bottom)

# Test case 4: Test switch with switch page
assert utils.confirm_switch(moving)

# Test case 5: Test switch with non-switch page
assert not utils.confirm_switch(top)

# Test case 6: Test switch with another switch page
assert utils.confirm_switch(moving2)

# Test case 7: Test switch with another non-switch page
assert not utils.confirm_switch(notPage)

