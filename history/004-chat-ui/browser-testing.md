# Browser Testing Instructions for Chat UI

## Test Setup

### Prerequisites
- Backend server running on http://127.0.0.1:8000
- Docusaurus development server running on http://localhost:3000

### Initial Setup
1. Start the backend server: `cd backend && python -m uvicorn src.main:app --reload`
2. Start the Docusaurus server: `cd physical-ai-book && npm run start`
3. Navigate to http://localhost:3000/chat

## Test Cases

### TC-001: Page Load Verification
**Objective**: Verify the chat page loads correctly
**Steps**:
1. Navigate to http://localhost:3000/chat
2. Verify the page loads without errors
3. Verify the header "Chat with Book Content" is visible
4. Verify the health indicator shows "Backend Connected"

**Expected Results**:
- Page loads successfully
- Header text is visible
- Health indicator shows connected status
- No JavaScript errors in console

### TC-002: Message Input and Submission
**Objective**: Verify message input and submission works
**Steps**:
1. Type "Hello, how are you?" in the message input field
2. Click the "Send" button
3. Verify loading state appears
4. Verify the message appears in the chat history
5. Verify the assistant response appears

**Expected Results**:
- Message appears on the right (user bubble)
- Loading indicator appears during processing
- Assistant response appears on the left
- No errors during the process

### TC-003: Enter-to-Send Functionality
**Objective**: Verify pressing Enter sends the message
**Steps**:
1. Type "Test message" in the input field
2. Press Enter key
3. Verify the message is submitted

**Expected Results**:
- Message is submitted when Enter is pressed
- Same behavior as clicking Send button

### TC-004: Top_k Selector
**Objective**: Verify top_k selector functionality
**Steps**:
1. Change the top_k value from 5 to 3 using the dropdown
2. Submit a query
3. Verify the response respects the top_k setting

**Expected Results**:
- Dropdown allows selection of values 1-10
- Value persists after selection
- API calls use the selected top_k value

### TC-005: Mode Toggle
**Objective**: Verify mode toggle functionality
**Steps**:
1. Select "Selected Text Only" mode from the dropdown
2. Verify the selected_text textarea appears
3. Enter text in the selected_text field
4. Submit a query
5. Switch back to "Retrieval" mode
6. Verify the selected_text field disappears

**Expected Results**:
- Mode selection works correctly
- Selected text field appears/disappears as expected
- API calls include selected_text when in selected-text-only mode

### TC-006: Source Display
**Objective**: Verify source display functionality
**Steps**:
1. Submit a query that returns sources
2. Verify the "Sources" section appears
3. Click "Show Content" for a source
4. Verify the content is displayed
5. Click "Hide Content"
6. Verify the content is hidden

**Expected Results**:
- Sources section shows with proper count
- Clickable URLs open in new tabs
- Scores are displayed
- Content can be shown/hidden

### TC-007: Health Indicator
**Objective**: Verify health indicator updates correctly
**Steps**:
1. Observe the initial health status
2. Submit a few queries
3. Verify health status updates appropriately

**Expected Results**:
- Shows correct status (healthy, degraded, unhealthy, or checking)
- Visual indicator reflects the status
- Updates after API interactions

### TC-008: Error Handling
**Objective**: Verify error handling works
**Steps**:
1. Try submitting an empty message
2. Verify appropriate error handling
3. Try invalid inputs if possible

**Expected Results**:
- Errors are displayed gracefully
- UI doesn't crash
- User is informed of the issue

### TC-009: Responsive Design
**Objective**: Verify UI works on different screen sizes
**Steps**:
1. Open developer tools and toggle device toolbar
2. Test on mobile screen size (375x667)
3. Test on tablet screen size (768x1024)
4. Test on desktop screen size

**Expected Results**:
- UI elements are properly sized
- Chat window is usable on all screen sizes
- No overlapping or cut-off elements

### TC-010: Existing Functionality Preservation
**Objective**: Verify existing Docusaurus functionality wasn't broken
**Steps**:
1. Navigate to other pages (e.g., /docs/intro, /blog)
2. Verify they load correctly
3. Verify navigation works properly

**Expected Results**:
- All existing pages load without issues
- Navigation menu works as expected
- No regressions in existing functionality

## Cross-Browser Testing

### Chrome (Latest)
- [ ] All functionality works as expected
- [ ] No console errors
- [ ] Responsive design works correctly

### Firefox (Latest)
- [ ] All functionality works as expected
- [ ] No console errors
- [ ] Responsive design works correctly

### Safari (Latest)
- [ ] All functionality works as expected
- [ ] No console errors
- [ ] Responsive design works correctly

### Edge (Latest)
- [ ] All functionality works as expected
- [ ] No console errors
- [ ] Responsive design works correctly

## Performance Testing

### Load Time
- [ ] Page loads in under 3 seconds
- [ ] Components render quickly
- [ ] No performance bottlenecks

### Memory Usage
- [ ] No memory leaks
- [ ] Memory usage remains stable after multiple interactions

## Accessibility Testing

### Keyboard Navigation
- [ ] All interactive elements are accessible via Tab key
- [ ] Focus indicators are visible
- [ ] Form elements can be operated via keyboard

### Screen Reader Compatibility
- [ ] Content is properly announced by screen readers
- [ ] Interactive elements have appropriate labels

## Final Verification

### Overall Assessment
- [ ] All functional requirements (FR-001 to FR-012) are satisfied
- [ ] UI is responsive and user-friendly
- [ ] Error handling is robust
- [ ] Performance is acceptable
- [ ] No breaking changes to existing functionality
- [ ] Code follows Docusaurus best practices
- [ ] Security measures are in place