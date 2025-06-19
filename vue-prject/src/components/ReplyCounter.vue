<template>
    <div class="text-center mt-5">
        <p class="fs-4">Replies received: {{ replies.length }}</p>
        
        <div class="input-group mb-3 w-50 mx-auto">
            <input 
                type="text"
                class="form-control"
                v-model="newReply"
                placeholder="Enter your reply"
                @keyup.enter="addReply"
            />

            <button class="btn btn-secondary" @click="addReply">
                    Add Reply
            </button>
        </div>

        <div class="text-start mt-4 w-50 mx-auto">
            <div v-for="(reply, index) in replies" :key="index" class="alert alert-light border shadow-sm">
                  {{reply}}
                  <button class="btn btn-sm btn-danger" @click="deleteReply(index)">
                       Delete
                  </button>
            </div>

        </div>

        <button class="btn btn-secondary me-2" @click="addReply">
              Add Reply
        </button>

        <!-- <button :class="buttonClass" @click="toggleTheme">
            Change Theme
        </button> -->

    </div>
</template>


<script>
  export default {
    name: 'ReplyCounter',
    data() {
        return {
            newReply: '',
            replies: []
        };
    },
    methods: {
        addReply() {
            const trimmed = this.newReply.trim();
            if (trimmed) {
                this.replies.push(trimmed);
                this.newReply = ''; // clear input
            }
        },
        deleteReply(index) {
            this.replies.splice(index, 1)
        }
        // addReply() {
        //     this.replies++;
        // }
    }
  };
</script>



<!-- <script>
  export default {
    name: 'ReplyCounter',
    data() {
        return {
            replies: 8,
            isPrimary: true
        };
    },
    computed: {
        buttonClass() {
            // return {
            //     // btn: true,
            //     // 'btn-primary': this.isPrimary,
            //     // 'btn-success': !this.isPrimary
                
            // }
            return this.isPrimary ? 'btn btn-primary' : 'btn btn-success';
        }
    },
    methods: {
        toggleTheme() {
            this.isPrimary = !this.isPrimary;           
        },
        addReply() {
            this.replies++;
        }
    },
  }
</script>

<style scoped>
   button {
    padding: 10px 20px;
    font-size: 16px;
   }
</style> -->