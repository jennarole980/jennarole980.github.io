// ============================================
// STEP 1: SELECT ALL TAB ELEMENTS
// ============================================

// Select all tab buttons
const tabs = document.querySelectorAll('.tab');

// Select all tab content sections
const tabContents = document.querySelectorAll('.tab-content');


// ============================================
// STEP 2: CREATE THE SWITCH TAB FUNCTION
// ============================================
// This function takes a tabId parameter (string) and switches to that tab
function switchTab(tabId) {

    // Remove 'active' class from all tab buttons
    tabs.forEach(tab => {
        tab.classList.remove('active');
    });

    // Hide all tab content sections
    tabContents.forEach(content => {
        content.classList.remove('active');
    });

    // Find the clicked tab button
    const selectedTab = document.querySelector(`[data-tab="${tabId}"]`);

    // Activate the tab button if it exists
    if (selectedTab) {
        selectedTab.classList.add('active');
    }

    // Find the corresponding tab content
    const selectedContent = document.querySelector(`#${tabId}`);

    // Show the content if it exists
    if (selectedContent) {
        selectedContent.classList.add('active');
    }
}


// ============================================
// STEP 3: ADD EVENT LISTENERS TO TAB BUTTONS
// ============================================

tabs.forEach(tab => {

    // Click event
    tab.addEventListener('click', function () {
        const tabId = tab.getAttribute('data-tab');
        switchTab(tabId);
    });

    // Hover effect
    tab.addEventListener('mouseenter', function () {
        if (!tab.classList.contains('active')) {
            tab.style.backgroundColor = '#eee';
        }
    });

    // Remove hover effect
    tab.addEventListener('mouseleave', function () {
        if (!tab.classList.contains('active')) {
            tab.style.backgroundColor = '';
        }
    });

});


// ============================================
// STEP 4: INITIALIZE THE TABS ON PAGE LOAD
// ============================================

document.addEventListener('DOMContentLoaded', function () {
    switchTab('home');
});