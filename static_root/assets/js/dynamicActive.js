
// Get the current page path
var currentPagePath = window.location.pathname;

// Select all menu items
var menuItems = document.querySelectorAll('.sub-menus li a');

// Iterate through menu items and add "active" class to the matching one
menuItems.forEach(function (menuItem) {
    // Extract the href attribute from the menu item
    var menuItemPath = new URL(menuItem.href).pathname;

    // Check if the current page path matches the menu item path
    if (currentPagePath === menuItemPath) {
        menuItem.classList.add('active');
    }
});        