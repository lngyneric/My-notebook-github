import json
import sys

def canvas_to_mermaid(canvas_file):
    try:
        with open(canvas_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        return f"Error loading file: {e}"

    nodes = data.get('nodes', [])
    edges = data.get('edges', [])

    # Map node IDs to their Mermaid representation ID (sanitized)
    # Mermaid IDs must be alphanumeric
    id_map = {}
    
    def clean_id(raw_id):
        return raw_id.replace('-', '_')

    for node in nodes:
        id_map[node['id']] = clean_id(node['id'])

    mermaid_lines = ["graph TD"]

    # Process Groups first to create subgraphs
    # We need to find which nodes are inside which groups
    # Logic: if node.x >= group.x and node.y >= group.y ...
    
    groups = [n for n in nodes if n['type'] == 'group']
    regular_nodes = [n for n in nodes if n['type'] != 'group']
    
    # Assign nodes to groups
    # A node is in a group if its center is inside the group
    node_group_map = {} # node_id -> group_id
    
    for node in regular_nodes:
        node_center_x = node['x'] + node['width'] / 2
        node_center_y = node['y'] + node['height'] / 2
        
        # Check containment (simple check, assume no nested groups for this script for simplicity, or pick smallest group)
        # Iterate groups, find one that contains center
        for group in groups:
            if (group['x'] <= node_center_x <= group['x'] + group['width'] and
                group['y'] <= node_center_y <= group['y'] + group['height']):
                node_group_map[node['id']] = group['id']
                break # Assign to first found group

    # Function to format node text for Mermaid
    def format_node(node):
        nid = id_map[node['id']]
        text = node.get('text', node.get('label', ''))
        # Escape quotes and newlines
        text = text.replace('"', "'")
        # Truncate or summarize text for display
        lines = text.split('\n')
        # Take header or first non-empty line
        display_text = ""
        for line in lines:
            if line.strip():
                display_text = line.strip()
                break
        if len(lines) > 1:
            display_text += "..."
        
        # Handle shape based on type?
        # Text nodes: box
        return f'{nid}["{display_text}"]'

    # Generate subgraphs
    processed_nodes = set()
    
    for group in groups:
        gid = id_map[group['id']]
        label = group.get('label', 'Group')
        mermaid_lines.append(f'    subgraph {gid} ["{label}"]')
        
        # Add nodes belonging to this group
        for node in regular_nodes:
            if node_group_map.get(node['id']) == group['id']:
                mermaid_lines.append(f'        {format_node(node)}')
                processed_nodes.add(node['id'])
        
        mermaid_lines.append('    end')

    # Add remaining nodes (not in any group)
    for node in regular_nodes:
        if node['id'] not in processed_nodes:
            mermaid_lines.append(f'    {format_node(node)}')

    # Add edges
    for edge in edges:
        from_id = id_map.get(edge['fromNode'])
        to_id = id_map.get(edge['toNode'])
        if from_id and to_id:
            label = edge.get('label', '')
            arrow = "-->"
            if label:
                arrow = f'-- "{label}" -->'
            mermaid_lines.append(f'    {from_id} {arrow} {to_id}')

    return "\n".join(mermaid_lines)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = r"C:\Users\lingyun\Documents\GOG\飞书快速收集信息AI判断方案-6f4014e6a1.canvas"
    print(canvas_to_mermaid(file_path))
