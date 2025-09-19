function showSection(id) {
            document.querySelectorAll('.form-section').forEach(el => el.classList.remove('active'));
            document.getElementById(id).classList.add('active');
            document.querySelectorAll('.nav-buttons button').forEach(btn => btn.classList.remove('active'));
            const index = Array.from(document.querySelectorAll('.form-section')).findIndex(x => x.id === id);
            if (index > -1)
                document.querySelectorAll('.nav-buttons button')[index].classList.add('active');
        }

        function generateProjects() {
            const count = parseInt(document.getElementById('projectCount').value) || 0;
            const container = document.getElementById('projectContainer');
            container.innerHTML = '';
            for (let i = 1; i <= count; i++) {
                const div = document.createElement('div');
                div.className = 'dynamic-project';
                div.innerHTML = `
          <div class="form-row">
            <div class="form-group">
              <label for="project${i}_name">Project ${i} - Name</label>
              <input type="text" name="project${i}_name" id="project${i}_name">
            </div>
            <div class="form-group">
              <label for="project${i}_keywords">Project ${i} - Keywords</label>
              <input type="text" name="project${i}_keywords" id="project${i}_keywords">
            </div>
          </div>
          <div class="form-row">
            <div class="form-group">
              <label for="project${i}_description">Project ${i} - Summary</label>
              <textarea name="project${i}_description" id="project${i}_description"></textarea>
            </div>
          </div>
        `;
                container.appendChild(div);
            }
        }

function generateresume(url){
      console.log('url'+ url);
      window.location.href = url;
}