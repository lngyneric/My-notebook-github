import json
import uuid
import time

def create_uuid():
    return str(uuid.uuid4())

def create_canvas_node(id, x, y, width, height, text, color="1"):
    return {
        "id": id,
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "type": "text",
        "text": text,
        "color": color
    }

def create_canvas_group(id, x, y, width, height, label, color="1"):
    return {
        "id": id,
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "type": "group",
        "label": label,
        "color": color
    }

def create_canvas_edge(id, from_node, to_node, label=None):
    edge = {
        "id": id,
        "fromNode": from_node,
        "fromSide": "bottom",
        "toNode": to_node,
        "toSide": "top"
    }
    if label:
        edge["label"] = label
    return edge

# Define content structure
nodes = []
edges = []

# --- Left Side: Training Reinforcement ---
# Group 1: Step 1
step1_group_id = create_uuid()
step1_x, step1_y = -400, -600
nodes.append(create_canvas_group(step1_group_id, step1_x - 20, step1_y - 40, 340, 600, "第一步 入职培训三天", "3"))

s1_nodes = [
    "新员工报到",
    "HR: 公司制度/合同/手册",
    "上司: MBO·责任田·经销商·框架·政策·产品·月会",
    "助理: CRM/报销/会议/战略报告",
    "参观+HR总监面谈"
]

prev_id = None
current_y = step1_y
for i, text in enumerate(s1_nodes):
    node_id = create_uuid()
    nodes.append(create_canvas_node(node_id, step1_x, current_y, 300, 80 if len(text)>20 else 50, text, "3"))
    if prev_id:
        edges.append(create_canvas_edge(create_uuid(), prev_id, node_id))
    prev_id = node_id
    current_y += 110
s1_end_id = prev_id

# Decision
decision_id = create_uuid()
nodes.append(create_canvas_node(decision_id, step1_x, current_y + 50, 300, 100, "身份是主管以上的一线员工?", "4"))
edges.append(create_canvas_edge(create_uuid(), s1_end_id, decision_id))

# Step 2: Small Stove
step2_group_id = create_uuid()
step2_x, step2_y = -400, current_y + 200
nodes.append(create_canvas_group(step2_group_id, step2_x - 20, step2_y - 40, 340, 700, "第二步 小灶培训", "3"))

s2_nodes = [
    "渠道管理",
    "市场政策",
    "招标数字管理",
    "客户管理",
    "团队管理",
    "逻辑与批判性思维"
]

prev_id = None
current_y = step2_y
s2_start_id = None
for text in s2_nodes:
    node_id = create_uuid()
    nodes.append(create_canvas_node(node_id, step2_x, current_y, 300, 50, text, "3"))
    if not s2_start_id: s2_start_id = node_id
    if prev_id:
        edges.append(create_canvas_edge(create_uuid(), prev_id, node_id))
    prev_id = node_id
    current_y += 100
s2_end_id = prev_id

# Link Decision to Step 2
edge = create_canvas_edge(create_uuid(), decision_id, s2_start_id, "是")
edges.append(edge)

# Step 3
step3_group_id = create_uuid()
step3_x, step3_y = 0, -600
nodes.append(create_canvas_group(step3_group_id, step3_x - 20, step3_y - 40, 340, 400, "第三步 新员工训练营", "3"))

s3_nodes = [
    "扫盲考自学+考试通过",
    "新人训练营课程3天集训",
    "结业考试+反馈"
]

prev_id = None
current_y = step3_y
for text in s3_nodes:
    node_id = create_uuid()
    nodes.append(create_canvas_node(node_id, step3_x, current_y, 300, 80, text, "3"))
    if prev_id:
        edges.append(create_canvas_edge(create_uuid(), prev_id, node_id))
    prev_id = node_id
    current_y += 120

connection_id = create_uuid()
nodes.append(create_canvas_node(connection_id, step3_x, current_y + 50, 300, 50, "衔接第一段结束", "5"))
edges.append(create_canvas_edge(create_uuid(), prev_id, connection_id))


# --- Right Side: Mentoring Plan ---
# Phase 1
phase1_group_id = create_uuid()
phase1_x, phase1_y = 400, -200
nodes.append(create_canvas_group(phase1_group_id, phase1_x - 20, phase1_y - 40, 340, 600, "阶段1_通用技能培训", "6"))

p1_nodes = [
    "上司（生免）/大客户带教",
    "学习企业文化",
    "通识扫盲考"
]

prev_id = None
current_y = phase1_y
p1_start_id = None
for text in p1_nodes:
    node_id = create_uuid()
    nodes.append(create_canvas_node(node_id, phase1_x, current_y, 300, 50, text, "6"))
    if not p1_start_id: p1_start_id = node_id
    if prev_id:
        edges.append(create_canvas_edge(create_uuid(), prev_id, node_id))
    prev_id = node_id
    current_y += 100

p1_decision_id = create_uuid()
nodes.append(create_canvas_node(p1_decision_id, phase1_x, current_y, 300, 80, "≥80分?", "4"))
edges.append(create_canvas_edge(create_uuid(), prev_id, p1_decision_id))

p1_yes_id = create_uuid()
nodes.append(create_canvas_node(p1_yes_id, phase1_x - 100, current_y + 150, 200, 50, "进入专业知识培训", "6"))
p1_no_id = create_uuid()
nodes.append(create_canvas_node(p1_no_id, phase1_x + 150, current_y + 150, 150, 50, "导师补强", "6"))

edges.append(create_canvas_edge(create_uuid(), p1_decision_id, p1_yes_id, "是"))
edges.append(create_canvas_edge(create_uuid(), p1_decision_id, p1_no_id, "否"))

# Link back for No
edge = create_canvas_edge(create_uuid(), p1_no_id, prev_id) # back to exam
edge["toSide"] = "right"
edge["fromSide"] = "top"
edges.append(edge)


# Connections from Left to Right
# Decision No -> Phase 1 Start
edge = create_canvas_edge(create_uuid(), decision_id, p1_start_id, "否")
edge["toSide"] = "left"
edge["fromSide"] = "right"
edges.append(edge)

# Step 2 End -> Phase 1 Start
edge = create_canvas_edge(create_uuid(), s2_end_id, p1_start_id)
edge["toSide"] = "left"
edge["fromSide"] = "right"
edges.append(edge)

# Step 3 Connection -> Phase 1 Start (Actually to Phase 2 connection, but flow suggests joining)
# In image: "衔接第一段结束" points to "阶段2_专业知识培训" top? Or "第二段结束"?
# Looking at image: "衔接第一段结束" points to "第二段结束". 
# Wait, "衔接第一段结束" is purple. "第二段结束" is purple.
# Let's assume flow: Step 3 -> Phase 2 connection.

p2_connection_id = create_uuid()
nodes.append(create_canvas_node(p2_connection_id, phase1_x, current_y + 250, 300, 50, "第二段结束", "5"))
edges.append(create_canvas_edge(create_uuid(), p1_yes_id, p2_connection_id))
edges.append(create_canvas_edge(create_uuid(), connection_id, p2_connection_id))

# Phase 2
phase2_group_id = create_uuid()
phase2_x, phase2_y = 800, -600
nodes.append(create_canvas_group(phase2_group_id, phase2_x - 20, phase2_y - 40, 340, 500, "阶段2_专业知识培训", "6"))

p2_nodes = [
    "上司（生免）/大客户带教",
    "产品&标准解读",
    "提交知识测试"
]

prev_id = None
current_y = phase2_y
p2_start_id = None
for text in p2_nodes:
    node_id = create_uuid()
    nodes.append(create_canvas_node(node_id, phase2_x, current_y, 300, 50, text, "6"))
    if not p2_start_id: p2_start_id = node_id
    if prev_id:
        edges.append(create_canvas_edge(create_uuid(), prev_id, node_id))
    prev_id = node_id
    current_y += 100

# Connect Phase 2 connection to Phase 2 start
edges.append(create_canvas_edge(create_uuid(), p2_connection_id, p2_start_id))

p2_decision_id = create_uuid()
nodes.append(create_canvas_node(p2_decision_id, phase2_x, current_y, 300, 80, "≥80分?", "4"))
edges.append(create_canvas_edge(create_uuid(), prev_id, p2_decision_id))

p2_yes_id = create_uuid()
nodes.append(create_canvas_node(p2_yes_id, phase2_x - 100, current_y + 150, 150, 50, "通知阶段完成", "6"))
p2_no_id = create_uuid()
nodes.append(create_canvas_node(p2_no_id, phase2_x + 150, current_y + 150, 150, 50, "额外辅导", "6"))

edges.append(create_canvas_edge(create_uuid(), p2_decision_id, p2_yes_id, "是"))
edges.append(create_canvas_edge(create_uuid(), p2_decision_id, p2_no_id, "否"))


# Phase 3
phase3_group_id = create_uuid()
phase3_x, phase3_y = 800, current_y + 250
nodes.append(create_canvas_group(phase3_group_id, phase3_x - 20, phase3_y - 40, 340, 600, "阶段3_岗位实操", "6"))

p3_nodes = [
    "安排实操任务",
    "实践操作",
    "现场指导",
    "提交实训报告"
]

prev_id = None
current_y = phase3_y
p3_start_id = None
for text in p3_nodes:
    node_id = create_uuid()
    nodes.append(create_canvas_node(node_id, phase3_x, current_y, 300, 50, text, "6"))
    if not p3_start_id: p3_start_id = node_id
    if prev_id:
        edges.append(create_canvas_edge(create_uuid(), prev_id, node_id))
    prev_id = node_id
    current_y += 100

# Connect Phase 2 Yes to Phase 3 Start
edges.append(create_canvas_edge(create_uuid(), p2_yes_id, p3_start_id))

p3_decision_id = create_uuid()
nodes.append(create_canvas_node(p3_decision_id, phase3_x, current_y, 300, 80, "考核通过?", "4"))
edges.append(create_canvas_edge(create_uuid(), prev_id, p3_decision_id))

p3_yes_id = create_uuid()
nodes.append(create_canvas_node(p3_yes_id, phase3_x - 100, current_y + 150, 150, 50, "正式录用", "6"))
p3_no_id = create_uuid()
nodes.append(create_canvas_node(p3_no_id, phase3_x + 150, current_y + 150, 150, 50, "终止", "6"))

edges.append(create_canvas_edge(create_uuid(), p3_decision_id, p3_yes_id, "是"))
edges.append(create_canvas_edge(create_uuid(), p3_decision_id, p3_no_id, "否"))

p3_end_id = create_uuid()
nodes.append(create_canvas_node(p3_end_id, phase3_x, current_y + 250, 300, 50, "第三段结束", "5"))
edges.append(create_canvas_edge(create_uuid(), p3_yes_id, p3_end_id))


canvas_data = {
    "nodes": nodes,
    "edges": edges
}

with open("c:\\Users\\lingyun\\Documents\\BaiduSyncdisk\\xcxnotes\\content\\Training_Flowchart.canvas", "w", encoding="utf-8") as f:
    json.dump(canvas_data, f, indent=4, ensure_ascii=False)

# --- Excalidraw Generation ---
# Simplistic Excalidraw generator
# Maps canvas nodes to rectangles and edges to arrows

excalidraw_elements = []

def create_ex_rect(id, x, y, w, h, text, bg_color="#ffffff"):
    return [
        {
            "id": id,
            "type": "rectangle",
            "x": x,
            "y": y,
            "width": w,
            "height": h,
            "backgroundColor": bg_color,
            "strokeColor": "#000000",
            "fillStyle": "solid",
            "strokeWidth": 1,
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "roundness": { "type": 3 },
            "boundElements": [{ "id": id + "_text", "type": "text" }]
        },
        {
            "id": id + "_text",
            "type": "text",
            "x": x + 10,
            "y": y + h/2 - 10,
            "width": w - 20,
            "height": 20,
            "text": text,
            "fontSize": 16,
            "fontFamily": 1,
            "textAlign": "center",
            "verticalAlign": "middle",
            "containerId": id
        }
    ]

def create_ex_arrow(id, start_x, start_y, end_x, end_y):
    return {
        "id": id,
        "type": "arrow",
        "x": start_x,
        "y": start_y,
        "width": end_x - start_x,
        "height": end_y - start_y,
        "strokeColor": "#000000",
        "points": [[0, 0], [end_x - start_x, end_y - start_y]]
    }

# Convert nodes
node_map = {} # id -> {x, y, w, h}
for node in nodes:
    if node["type"] == "group":
        continue # Skip groups for simplicity or draw them first as background
    
    bg_color = "#ffffff"
    if node.get("color") == "3": bg_color = "#fff5e6" # Orangeish
    if node.get("color") == "6": bg_color = "#e6f2ff" # Blueish
    
    elems = create_ex_rect(node["id"], node["x"] + 1000, node["y"] + 1000, node["width"], node["height"], node["text"], bg_color)
    excalidraw_elements.extend(elems)
    node_map[node["id"]] = {"x": node["x"] + 1000, "y": node["y"] + 1000, "w": node["width"], "h": node["height"]}

# Convert edges
for edge in edges:
    from_n = node_map.get(edge["fromNode"])
    to_n = node_map.get(edge["toNode"])
    
    if from_n and to_n:
        # Simple center-to-center arrow
        start_x = from_n["x"] + from_n["w"] / 2
        start_y = from_n["y"] + from_n["h"]
        end_x = to_n["x"] + to_n["w"] / 2
        end_y = to_n["y"]
        
        excalidraw_elements.append(create_ex_arrow(edge["id"], start_x, start_y, end_x, end_y))

excalidraw_data = {
    "type": "excalidraw",
    "version": 2,
    "source": "https://excalidraw.com",
    "elements": excalidraw_elements,
    "appState": {
        "viewBackgroundColor": "#ffffff",
        "gridSize": 20
    }
}

with open("c:\\Users\\lingyun\\Documents\\BaiduSyncdisk\\xcxnotes\\content\\Training_Flowchart.excalidraw", "w", encoding="utf-8") as f:
    json.dump(excalidraw_data, f, indent=4, ensure_ascii=False)

print("Files created.")
