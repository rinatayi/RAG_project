# backend/app/services/rag_service.py
from typing import Dict, Any

async def call_lightrag_search(query: str, scenario: str) -> Dict[str, Any]:
    """
    呼叫 LightRAG 向量與知識圖譜雙層檢索[cite: 3]
    """
    # 依情境帶入預設對應的 LightRAG 檢索內容與引用標籤[cite: 3]
    if scenario == "compliance_planning":
        context = "【法規】高架作業勞工保護措施標準第3條：雇主使勞工於高度5公尺以上從事鋼構施工作業，應設置護欄、防墜網或使勞工佩戴全身式安全帶。【SOP】公司SOP-5-2未規定施工架竣工檢查表。"
        sources = [
            {"source_title": "高架作業勞工保護措施標準 第3條", "file_id": "LAW-001"},
            {"source_title": "公司SOP-5-2", "file_id": "SOP-5-2"}
        ]
    elif scenario == "sop_check":
        context = "【法規】高架作業勞工保護措施標準第4條：雇主應依作業高度安排勞工適當休息時間。【SOP】SOP-5-2第五條未具體標明休息時數。"
        sources = [
            {"source_title": "高架作業勞工保護措施標準 第4條", "file_id": "LAW-001"},
            {"source_title": "公司SOP-5-2", "file_id": "SOP-5-2"}
        ]
    elif scenario == "incident_analysis":
        context = "【歷史事故】ACC-2024-08 地面濕滑導致跌倒，改善措施加裝防滑踏板未完成；ACC-2023-11 照明不足。設施規則第225條。"
        sources = [
            {"source_title": "事故紀錄 ACC-2024-08", "file_id": "ACC-2024-08"},
            {"source_title": "事故紀錄 ACC-2023-11", "file_id": "ACC-2023-11"},
            {"source_title": "職業安全衛生設施規則 第225條", "file_id": "LAW-002"}
        ]
    else:  # prework_check
        context = "【人員與設備】員工A教育訓練正常，員工B高空作業教育訓練已於上月逾期。安全帶已配發，工作許可已核發。"
        sources = [
            {"source_title": "高架作業勞工保護措施標準 第7條", "file_id": "LAW-001"},
            {"source_title": "公司SOP-5-2", "file_id": "SOP-5-2"},
            {"source_title": "教育訓練紀錄", "file_id": "HR-2026"}
        ]
        
    return {"context": context, "sources": sources}

async def call_ollama_llm(prompt: str) -> str:
    """
    呼叫地端 Ollama LLM 生成推理回答[cite: 3]
    """
    # 待地端連線後替換為 API 請求，目前直接返回組好的 Prompt 邏輯
    return "已依據 LightRAG 知識圖譜與法規庫完成分析。"