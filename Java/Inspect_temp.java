public class Inspect {
	public static void main(String[] args) {
		System.out.println("start");
		String i = "5";
		inspect(i);
		System.out.println("end");
		
	}

	public static void inspect (Object t1){
		Class classID = t1.getClass();
		Object[] field = classID.getFields();
		Object[] method = classID.getMethods();
		
		System.out.println("Name = " + classID.getName());
		System.out.println("Packege = " + classID.getPackage().toString());
		for (int i=0; i < method.length ;i++)
			System.out.println("Method = " + method[i].toString());
		for (int i=0; i < field.length ;i++)
			System.out.println("Field = " + field[i].toString());
	}
}