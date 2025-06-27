from nicegui import ui, app

def create():
    @ui.page('/')
    def index():
        # Initialize counter in user storage to persist across page reloads
        if 'counter' not in app.storage.user:
            app.storage.user['counter'] = 0
        
        # Create the main container with centered layout  
        with ui.column().classes('items-center justify-center min-h-screen gap-8'):
            ui.label('Counter Application').classes('text-4xl font-bold text-center mb-4').mark('title')
            
            # Counter display
            counter_display = ui.label().classes('text-6xl font-bold text-blue-600 text-center').mark('counter-display')
            
            # Button container
            with ui.row().classes('gap-4'):
                decrement_btn = ui.button('-', 
                    color='red', 
                    icon='remove'
                ).classes('text-2xl px-8 py-4').mark('decrement-btn')
                
                increment_btn = ui.button('+', 
                    color='green', 
                    icon='add'
                ).classes('text-2xl px-8 py-4').mark('increment-btn')
            
            # Reset button
            reset_btn = ui.button('Reset', 
                color='gray', 
                icon='refresh'
            ).classes('px-6 py-2 mt-4').mark('reset-btn')
        
        def update_display():
            """Update the counter display with current value"""
            counter_display.set_text(str(app.storage.user['counter']))
        
        def increment():
            """Increment counter and update display"""
            app.storage.user['counter'] += 1
            update_display()
            ui.notify(f'Counter incremented to {app.storage.user["counter"]}', type='positive')
        
        def decrement():
            """Decrement counter and update display"""
            app.storage.user['counter'] -= 1
            update_display()
            ui.notify(f'Counter decremented to {app.storage.user["counter"]}', type='info')
        
        def reset():
            """Reset counter to zero"""
            app.storage.user['counter'] = 0
            update_display()
            ui.notify('Counter reset to 0', type='warning')
        
        # Connect button handlers
        increment_btn.on_click(increment)
        decrement_btn.on_click(decrement)
        reset_btn.on_click(reset)
        
        # Initial display update
        update_display()