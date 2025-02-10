from IPython.display import display, Javascript

def create_popup(message, title="Notice"):
    """
    Create and display a popup in a Jupyter notebook.
    
    Args:
        message (str): The message to display in the popup
        title (str, optional): The title of the popup. Defaults to "Notice"
    """
    js_code = f"""
        // Create backdrop
        const backdrop = document.createElement('div');
        backdrop.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(0,0,0,0.5);
            z-index: 999;
        `;
        
        // Create container for our popup
        const popup = document.createElement('div');
        popup.style.cssText = `
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            padding: 2rem;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            z-index: 1000;
            color: black;
            max-height: 80vh;
            max-width: 80vw;
            overflow-y: auto;
            -webkit-overflow-scrolling: touch;
        `;
        
        // Add HTML content
        popup.innerHTML = `
            <div style="position: absolute; top: 10px; right: 10px; cursor: pointer; font-size: 20px; 
                width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; 
                border-radius: 50%; hover: background-color: #f0f0f0;"
                onclick="this.closest('.popup-container').remove()">
                ✕
            </div>
            <h2 style="margin-top: 5px; margin-right: 30px;">{title}</h2>
            <div style="margin: 20px 0;">
                <p>{message}</p>
            </div>
        `;
        
        // Create a container for both backdrop and popup
        const container = document.createElement('div');
        container.className = 'popup-container';
        container.appendChild(backdrop);
        container.appendChild(popup);
        
        // Add close functionality to backdrop
        backdrop.onclick = () => container.remove();
        
        // Add to document
        document.body.appendChild(container);
    """
    
    display(Javascript(js_code))