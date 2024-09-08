vector<ListNode*>sol;
        int len=length(head);
        vector<int>cnt;
        int div=len/k;
        int mod=len%k;
        for(int i=0;i<mod;i++){
            cnt.push_back(div+1);
        }
        for(int i=0;i<k-mod;i++){
            cnt.push_back(div);
        }
        // for(int i:cnt) cout<<i<<"\t";
        ListNode* temp=head;
        int loc=0;
        ListNode* bs=temp;
        for(int i:cnt){
            while(loc!=i){
                temp=bs;
                bs=bs->next;
                loc+=1;
            }
            if(temp)
            temp->next=nullptr;
            if(head){
                sol.push_back(head);
                head=bs;
                temp=bs;
            }
            else{
                sol.push_back(nullptr);
            }
            loc=0;
        }
        while(sol.size()<k){
            sol.push_back(nullptr);
        }
        return sol;
