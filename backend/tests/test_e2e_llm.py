# backend/tests/test_e2e_llm.py
import asyncio
import os
import sys
import traceback

# 1. 優先將 backend 目錄（即當前檔名的上一層目錄）加入 sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 2. 接著才匯入專案內部模組
from app.services.rag_service import generate_rag_response

async def test_full_rag_pipeline():
    print("=== 開始測試 端到端 RAG + Ollama 生成管道 ===")
    
    test_query = "雇主未提供必要的安全衛生設備或措施，導致勞工發生重大職業災害時，會面臨什麼法律責任？"
    scenario = "compliance_planning"
    model = "llama3"  # 請依你地端 Ollama 已下載的模型名稱調整（如 llama3, qwen2.5 等）
    
    print(f"[1/3] 發送問題: '{test_query}' (情境: {scenario})")
    
    try:
        res = await generate_rag_response(query=test_query, scenario=scenario, model=model)
        
        print("✓ RAG 流程執行成功！")
        print(f"  - 檢索到的 Context 長度: {res['context_length']} 字")
        print("-" * 50)
        print("【Ollama 最終生成回答】")
        print(res["response"])
        print("-" * 50)
        
        assert len(res["response"]) > 0, "LLM 回答不應為空"
        print("✓ 端到端測試完成！")
        
    except Exception as e:
        print(f"❌ 測試失敗: {e}")
        print("-" * 50)
        traceback.print_exc()
        print("-" * 50)

if __name__ == "__main__":
    asyncio.run(test_full_rag_pipeline())
